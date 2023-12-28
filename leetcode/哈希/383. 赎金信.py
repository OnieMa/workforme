class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # maaoyu
        cot = list(magazine)
        for r in ransomNote:
            if r in cot:
                cot.remove(r)

            else:
                return False
        return True


    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = [0] * 26
        magazine_count = [0] * 26
        for c in ransomNote:
            ransom_count[ord(c) - ord('a')] += 1
        for c in magazine:
            magazine_count[ord(c) - ord('a')] += 1
        return all(ransom_count[i] <= magazine_count[i] for i in range(26))


if __name__ == '__main__':
    Solution().canConstruct("aa", "aba")
