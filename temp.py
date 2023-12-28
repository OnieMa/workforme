import heapq
from collections import deque
from typing import List


class Solution(object):
    def topKFrequent(self, nums, k):
        map_ = dict()
        for i in nums:
            map_[i] = map_.get(i, 0) + 1

        # 对频率排序
        # 定义一个小顶堆，大小为k
        pri_que = []  # 小顶堆

        # 用固定大小为k的小顶堆，扫描所有频率的数值
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k:  # 如果堆的大小大于了K，则队列弹出，保证堆的大小一直为k
                heapq.heappop(pri_que)

        # 找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组
        # result = [0] * k
        # for i in range(k - 1, -1, -1):
        #     result[i] = heapq.heappop(pri_que)[1]
        # return result

        # 因为返回的元素的顺序无所谓 所以堆中剩下的就是结果
        result = [0] * k
        for i in range(k):
            result[i] = heapq.heappop(pri_que)

        return result


if __name__ == '__main__':
    Solution().topKFrequent([1, 1, 1, 2, 3, 3], 2)
