from typing import Optional


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


"""
给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和
#  targetSum 。如果存在，返回 true ；否则，返回 false 。 
"""


class Solution:
	def iterate(self, cur: TreeNode, count: int) -> bool:
		if not cur.left and not cur.right and count == 0:
			return True  # 符合条件 直接返回
		if not cur.left and not cur.right:
			return False  # 到达子节点 应该直接返回

		if cur.left:
			count -= cur.left.val
			if self.iterate(cur.left, count):  # 递归 处理节点
				return True
			count += cur.left.val  # 回溯
		if cur.right:
			count -= cur.right.val
			if self.iterate(cur.right, count):  # 递归 处理节点
				return True
			count += cur.right.val  # 回溯
		return False

	def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
		if not root:
			return False
		return self.iterate(root, targetSum - root.val)
