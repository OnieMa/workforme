from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 二叉树的最大深度
class Solution(object):
    def maxDepth(self, root):
        dep = 0
        if not root:
            return dep

        queue = deque([root])
        while queue:
            dep += 1
            for _ in range(len(deque)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return dep

    # 最小的深度
    def minDepth(self, root):
        dep = 0
        if not root:
            return dep
        queue = deque([root])
        while deque:
            dep += 1
            for _ in range(len(deque)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if not node.left and not node.right:
                    return dep
        return dep