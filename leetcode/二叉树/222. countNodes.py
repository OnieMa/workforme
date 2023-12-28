from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def countNodes1(self, root):
        count = 0
        if not root:
            return count

        queue = deque([root])
        while queue:
            node = queue.popleft()
            for _ in range(len(queue)):
                if node.left:
                    queue.append(node.left)
                    count += 1
                if node.right:
                    queue.append(node.right)
                    count += 1
        return count

    def getNodes(self, root):
        if not root:
            return 0
        leftNum = self.getNodes(root.left)
        rightNum = self.getNodes(root.right)
        return 1 + leftNum + rightNum

    def countNodes(self, root):
        return self.getNodes(root)
