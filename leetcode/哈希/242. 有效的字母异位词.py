class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        nums = [0] * 26

        for i in s:
            nums[ord(i) - ord('a')] += 1
            print(nums)
        for i in t:
            nums[ord(i) - ord('a')] -= 1
            print(nums)

        for i in range(26):
            if nums[i] != 0:
                return False
        return True


if __name__ == '__main__':
    Solution().isAnagram("rat", "car")
