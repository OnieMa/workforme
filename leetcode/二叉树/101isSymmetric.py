from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归法
class Solution1(object):
    def isSymmetric(self, root):
        if not root:
            return True

    def compare(self, left, right):
        # 判断有None的情况
        if left and not right:
            return False
        elif not left and right:
            return False
        elif not left and not right:
            return True
        elif left.val != right.val:
            return False

        # 此时是双节点都不为空 而且相等的情况
        outside = self.compare(left.left, right.right)
        inside = self.compare(left.right, right.left)
        return outside and inside


# 迭代法
class Solution(object):
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = deque()
        queue.append(root.left)  # 将左子树头结点加入队列
        queue.append(root.right)  # 将右子树头结点加入队列
        while queue:  # 接下来就要判断这这两个树是否相互翻转
            leftNode = queue.popleft()
            rightNode = queue.popleft()
            if not leftNode and not rightNode:  # 左节点为空、右节点为空，此时说明是对称的
                continue

            # 左右一个节点不为空，或者都不为空但数值不相同，返回false
            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False
            queue.append(leftNode.left)  # 加入左节点左孩子
            queue.append(rightNode.right)  # 加入右节点右孩子
            queue.append(leftNode.right)  # 加入左节点右孩子
            queue.append(rightNode.left)  # 加入右节点左孩子
        return True

"""
        1
       / \
      2   2
     / \ / \
    3  4 4  3
   / \ /\ /\ /\
        55666655
        

"""