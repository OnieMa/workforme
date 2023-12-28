from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        print(nums)
        idx = 0
        left = 1
        right = len(nums) - 1

        # [-4, -1, -1, 0, 1, 2]
        while idx < len(nums) - 2:
            if left == right:
                idx += 1
                left = idx + 1
                right = len(nums) - 1
            if nums[idx] + nums[left] + nums[right] == 0:
                res.append([nums[idx], nums[left], nums[right]])
                idx += 1
            elif nums[idx] + nums[left] + nums[right] > 0:
                right -= 1
            elif nums[idx] + nums[left] + nums[right] < 0:
                left += 1
        return res



    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            # 如果第一个元素已经大于0，不需要进一步检查
            if nums[i] > 0:
                return result

            # 跳过相同的元素以避免重复
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while right > left:
                sum_ = nums[i] + nums[left] + nums[right]
                if sum_ < 0:
                    left += 1
                elif sum_ > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # 跳过相同的元素以避免重复
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1
                    right -= 1
                    left += 1

        return result


if __name__ == '__main__':
    print(Solution().threeSum([-4, -1, -1, 0, 1, 3, 3, 7]))
