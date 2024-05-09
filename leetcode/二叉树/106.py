from typing import List, Optional


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	# 从中序和后序遍历序列构建二叉树
	def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
		# 第一步 先处理特殊情况 树为空
		if not postorder:
			return None
		# 第二步 后序遍历的最后一个节点就是当前的中间节点
		root_val = postorder[-1]
		root = TreeNode(root_val)

		# 第三步 找到切割点
		separator_idx = inorder.index(root_val)

		# 第四步 切割inorder数组 得到inorder数组的左右边
		inorder_left = inorder[:separator_idx]
		inorder_right = inorder[separator_idx + 1:]

		# 第五步 切割postorder数组 得到postorder的左右半边
		### 重点 中序数组的大小和后序数组的大小是相同的
		postorder_left = postorder[:len(inorder_left)]
		postorder_right = postorder[len(inorder_left): len(postorder) - 1]

		# 第六步: 递归
		root.left = self.buildTree(inorder_left, postorder_left)
		root.right = self.buildTree(inorder_right, postorder_right)
		# 第七步: 返回答案
		return root
