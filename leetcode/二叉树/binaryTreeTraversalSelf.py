# 前序遍历-递归-LC144_二叉树的前序遍历
# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # 广度遍历  层级遍历
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        def eachLayer(node, level, result):
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            if node.left:
                eachLayer(node.left, level + 1, result)
            if node.right:
                eachLayer(node.right, level + 1, result)

        result = []
        eachLayer(root, 0, result)
        return [val for sub in result for val in sub]

    def rightSideView(self, root):
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            queue_length = len(queue)
            level = []
            for i in range(queue_length):
                node = queue.popleft()
                if i == queue_length - 1:
                    level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result

    def levelOrderTraversalIterationMethod(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []

        def get_level(root: TreeNode, level, result):
            if len(result) == level:
                result.append([])
            result[level].append(root.val)
            if root.left:
                get_level(root.left, level + 1, result)
            if root.right:
                get_level(root.right.root, level + 1, result)

        get_level(root, 0, result)
        return result


if __name__ == '__main__':
    # 创建树的节点
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(4)
    node4 = TreeNode(5)

    # 构建树的结构
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4

    print(Solution().rightElevation(root))

"""
        1
      /   \
     2     3
   /  \
 4     5
"""
