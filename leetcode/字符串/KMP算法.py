class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def KMP(s, p):
            """
            s为主串
            p为模式串
            如果t里有p，返回打头下标
            """
            nex = getNext(p)
            i = 0
            j = 0  # 分别是s和p的指针
            while i < len(s) and j < len(p):
                if j == -1 or s[i] == p[j]:  # j==-1是由于j=next[j]产生
                    i += 1
                    j += 1
                else:
                    j = nex[j]

            if j == len(p):  # j走到了末尾，说明匹配到了
                return i - j
            else:
                return -1

        def getNext(p):
            """
            p为模式串
            返回next数组，即部分匹配表
            """
            nex = [0] * len(p)
            nex[0] = -1
            i, j = 0, -1
            while i < len(p) - 1:
                if j == -1 or p[i] == p[j]:
                    i += 1
                    j += 1
                    nex[i] = j  # 这是最大的不同：记录next[i]
                else:
                    j = nex[j]
            return nex

        return KMP(haystack, needle)
