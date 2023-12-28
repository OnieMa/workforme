from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 快慢指针
        fast = 0  # 快指针
        slow = 0  # 慢指针
        size = len(nums)
        while fast < size:  # 不加等于是因为，a = size 时，nums[a] 会越界
            # slow 用来收集不等于 val 的值，如果 fast 对应值不等于 val，则把它与 slow 替换
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
            print(nums)
        return slow


if __name__ == '__main__':
    so = Solution()
    nums = [0, 0, 0, 1, 2, 2, 3, 3, 4, 5]

    """移除指定元素 返回列表前面的元素不变"""


    def removeElement(self, nums: List[int], val: int) -> int:
        slow, fast = 0, 0
        size = len(nums)
        while fast < size:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
