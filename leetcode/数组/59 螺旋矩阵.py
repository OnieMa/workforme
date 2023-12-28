"""
59.螺旋矩阵II
力扣题目链接(opens new window)

给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3 输出: [ [ 1, 2, 3 ], [ 8, 9, 4 ], [ 7, 6, 5 ] ]
"""
from typing import List


# 正确的二分法一定要坚持循环不变量原则。 本题就是找出循环不变量原则

class Solution:

    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0] * n for _ in range(n)]
        startx, starty = 0, 0  # 起始点
        loop, mid = n // 2, n // 2  # 迭代次数、n为奇数时，矩阵的中心点
        count = 1  # 计数

        for offset in range(1, loop + 1):  # 每循环一层偏移量加1，偏移量从1开始
            for i in range(starty, n - offset):  # 从左至右，左闭右开
                nums[startx][i] = count
                count += 1
            for i in range(startx, n - offset):  # 从上至下
                nums[i][n - offset] = count
                count += 1
            for i in range(n - offset, starty, -1):  # 从右至左
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, startx, -1):  # 从下至上
                nums[i][starty] = count
                count += 1
            startx += 1  # 更新起始点
            starty += 1

        if n % 2 != 0:  # n为奇数时，填充中心点
            nums[mid][mid] = count
        return nums


if __name__ == '__main__':
    # 11.15
    # def generateMatrix1(n: int) -> List[List[int]]:
    #     nums = [[0 for _ in range(n)] for _ in range(n)]
    #     startx, starty = 0, 0
    #     loop = n // 2  # 深度
    #     mid = n // 2  # 中心点位
    #     count = 1  # 起始数字
    #
    #     for offset in (1, loop + 1):
    #         for i in range(starty, n - offset):
    #             nums[starty][i] = count
    #             count += 1
    #
    #         for i in range(startx, n - offset):
    #             nums[i][n - offset] = count
    #             count += 1
    #
    #         for i in range(n - offset, starty, -1):
    #             nums[n - offset][i] = count
    #             count += 1
    #
    #         for i in range(n - offset, startx, -1):
    #             nums[i][startx] = count
    #             count += 1
    #
    #         startx += 1
    #         starty += 1
    #
    #     if loop % 2 != 0:
    #         nums[mid][mid] = count
    #
    #     return nums

    # 11.20
    def generateMatrix2(n: int) -> List[List[int]]:
        startx, starty = 0, 0
        loop = n // 2
        mid = n // 2
        count = 1  # 起始数字
        res = [[0] * n for _ in range(n)]
        for offset in range(loop):
            for i in range(starty, n - offset - 1):
                res[starty][i] = count
                count += 1
            for i in range(startx, n - offset - 1):
                res[i][n - offset - 1] = count
                count += 1
            for i in range(n - offset - 1, starty, -1):
                res[n - offset - 1][i] = count
                count += 1
            for i in range(n - offset - 1, startx, -1):
                res[i][startx] = count
                count += 1
            startx += 1
            starty += 1

        if n % 2 == 1:
            res[mid][mid] = count

        return res


    print(generateMatrix2(1))
