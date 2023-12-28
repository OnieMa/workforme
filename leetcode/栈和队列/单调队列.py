from collections import deque
from typing import Optional


class MyQueue:  # 单调队列（从大到小
    def __init__(self):
        self.queue = deque()  # 这里需要使用deque实现单调队列，直接使用list会超时

    # 每次弹出的时候，比较当前要弹出的数值是否等于队列出口元素的数值，如果相等则弹出。
    # 同时pop之前判断队列当前是否为空。
    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.popleft()  # list.pop()时间复杂度为O(n),这里需要使用collections.deque()
            # 如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出，直到push的数值小于等于队列入口元素的数值为止。

    # 这样就保持了队列里的数值是单调从大到小的了。
    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    # 查询当前队列里的最大值 直接返回队列前端也就是front就可以了。
    def front(self):
        return self.queue[0]


class MonotonicQueue():
    def __init__(self):
        self.que = deque()

    def pop(self, x):
        if self.que and x == self.que[0]:
            self.que.popleft()

    def push(self, x):
        while self.que and self.que[-1] < x:
            self.que.pop()
        self.que.append(x)

    def get_max(self):
        return self.que[0]


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        res = []
        qu = MonotonicQueue()
        for i in range(k):
            qu.push(i)
        res.append(qu.get_max())

        for i in range(k, len(nums)):
            qu.pop(nums[i-k])
            qu.push(nums[k])
            res.append(qu.get_max())
        return res

