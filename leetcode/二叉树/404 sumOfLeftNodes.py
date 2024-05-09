# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
		if not root:
			return 0
		result = 0
		queue = deque([root])
		while queue:
			node = queue.popleft()
			if node.left and node.left.left is None and node.left.right is None:
				result += node.left.val
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
		return result

	# 递归法实现
	def sumOfLeftLeavesByIter(self, root):
		if root is None:
			return 0
		if root.left is None and root.right is None:
			return 0

		leftValue = self.sumOfLeftLeaves(root.left)  # 左
		if root.left and not root.left.left and not root.left.right:  # 左子树是左叶子的情况
			leftValue = root.left.val

		rightValue = self.sumOfLeftLeaves(root.right)  # 右

		sum_val = leftValue + rightValue  # 中
		return sum_val

	def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
		result = 0
		if not root:
			return result
		queue = deque([root])
		while queue:
			que_len = len(queue)
			for i in range(que_len):
				node = queue.popleft()
				if i == 0:
					result = node.val
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)
		return result

	def findBottomLeftValueByRecursion(self, root: TreeNode) -> int:
		self.max_depth = float('-inf')
		self.result = None
		self.traversal(root, 0)
		return self.result

	def traversal(self, node, depth):
		if not node.left and not node.right:
			if depth > self.max_depth:
				self.max_depth = depth
				self.result = node.val
			return

		if node.left:
			depth += 1
			self.traversal(node.left, depth)
			depth -= 1
		if node.right:
			depth += 1
			self.traversal(node.right, depth)
			depth -= 1
