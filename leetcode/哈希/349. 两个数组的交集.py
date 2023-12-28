from typing import List


class Solution:
    def intersection1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = {}
        for num in nums1:
            table[num] = 0

        res = set()
        for num in nums2:
            if num in table:
                res.add(num)
                del table[num]

        return list(res)
        print(list(res))


if __name__ == '__main__':
    print(Solution().intersection([1, 2, 2, 1], [2, 2]))
