from typing import Optional, List


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


"""
找到所有符合目标值的路径数组  路径总和ii
"""


class Solution:
	def __init__(self):
		self.result = []
		self.path = []

	# 遍历
	def traversal(self, cur, count):
		# 到达叶节点 且count已经为0 代表找到了路径
		if not cur.left and not cur.right and count == 0:
			self.result.append(self.path[:])
			return
		# 到达叶节点 但是没有找到合适的路径 就直接返回
		if not cur.left and not cur.right:
			return

		if cur.left:  # 左 （空节点不遍历）
			self.path.append(cur.left.val)
			count -= cur.left.val
			self.traversal(cur.left, count)  # 递归
			count += cur.left.val  # 回溯
			self.path.pop()  # 回溯

		if cur.right:  # 右 （空节点不遍历）
			self.path.append(cur.right.val)
			count -= cur.right.val
			self.traversal(cur.right, count)  # 递归
			count += cur.right.val  # 回溯
			self.path.pop()  # 回溯

		return

	def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
		self.result.clear()
		self.path.clear()
		if not root:
			return self.result
		self.path.append(root.val)  # 把根节点放进路径
		self.traversal(root, targetSum - root.val)
		return self.result
