
class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        res = dict()

        # 现将前两个列表中所有的元素组合都放入dict中
        for i in nums1:
            for j in nums2:
                if i + j in res:
                    res[i + j] += 1
                else:
                    res[i + j] = 1

        print(res)
        count = 0
        # 取目标值的相反数
        for a in nums3:
            for b in nums4:
                key = -a - b
                if key in res:
                    count += res[key]
        return count


if __name__ == '__main__':
    print(Solution().fourSumCount([1, 1], [1, 1], [-1, -1], [-1, -1]))
