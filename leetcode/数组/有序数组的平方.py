from typing import List


# 27
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        k = len(nums) - 1
        result = [0] * len(nums)
        while left <= right:
            if nums[left] ** 2 > nums[right] ** 2:
                result[k] = nums[left] ** 2
                left += 1
            else:
                result[k] = nums[right] ** 2
                right -= 1
            k -= 1
        return result


if __name__ == '__main__':
    print(Solution().sortedSquares([-7, -3, 2, 3, 11]))


    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        res = [0] * len(nums)
        k = len(nums) - 1  # 新数组的索引
        while left <= right:
            if nums[left] ** 2 > nums[right] ** 2:
                res[k] = nums[left] ** 2
                left += 1
            else:
                res[k] = nums[right] ** 2
                right -= 1
            k -= 1
        return res
