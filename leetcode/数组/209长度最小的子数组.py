"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。

示例：

输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
提示：

1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
"""
from typing import List


# 滑动窗口

class Solution:
    def minSubArrayLen1(self, s: int, nums: List[int]) -> int:
        l = len(nums)
        left = 0
        right = 0
        min_len = float('inf')
        cur_sum = 0  # 当前的累加值

        while right < l:
            cur_sum += nums[right]

            while cur_sum >= s:  # 当前累加值大于目标值
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1

            right += 1

        return min_len if min_len != float('inf') else 0

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left, right = 0, 0
        l = len(nums)
        sum = 0
        min_len = float('inf')
        while right < l:
            sum += nums[right]
            while sum >= s:
                min_len = min(min_len, right - left + 1)
                # 先计算总和 再操作指针的移动
                sum -= nums[left]
                left += 1
            right += 1

        return min_len if min_len != float('inf') else 0


if __name__ == '__main__':
    # 11.15   [2,3,1,2,4,3]
    def minSubArrayLen3(self, s: int, nums: List[int]) -> int:
        left, right = 0, 0
        sums = 0
        min_len = float('inf')
        while right < len(nums):
            sums += nums[right]
            while sums > s:
                min_len = min(min_len, right - left + 1)
                sums -= nums[left]
                left += 1
            right += 1

        return min_len if min_len != float('inf') else 0


    # 11.20   [2,3,1,2,4,3]
    def minSubArrayLen4(self, s: int, nums: List[int]) -> int:
        left, right = 0, 0
        min_len = float('inf')
        nums_len = len(nums)
        sum = 0
        while right < nums_len:
            sum += nums[right]
            # if sum >= s:
            while sum >= s:
                min_len = min(min_len, right - left + 1)
                sum -= nums[left]
                left += 1
            right += 1

        return min_len if min_len != float('inf') else 0
