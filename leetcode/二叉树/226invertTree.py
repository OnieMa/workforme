# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        if not root:
            return []

        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                node.right, node.right = node.left, node.right
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root

