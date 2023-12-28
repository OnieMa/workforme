class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        numsLength = len(nums)
        res = []
        for i in range(numsLength):
            if 0 < target < nums[i]:
                break
            if i >= 1 and nums[i] == nums[i - 1]:
                continue

            index = i + 1
            left = index + 1
            right = numsLength - 1

            while index < numsLength - 2:
                # 剪枝 可以不做
                if nums[i] + nums[index] > target > 0:
                    break
                # 去重 是必须要做的 结果不可以包含重复数组
                if nums[index] == nums[index - 1] and index > i + 1:  # 在 > i+1 的时候 才能与前一位进行比较
                    continue

                while left < right:
                    sum = nums[i] + nums[index] + nums[left] + nums[right]
                    if sum > target:
                        right -= 1
                    elif sum < target:
                        left += 1
                    else:
                        res.append([nums[i], nums[index], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right += 1
        return res
