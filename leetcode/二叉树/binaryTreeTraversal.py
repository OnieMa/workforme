# 前序遍历-递归-LC144_二叉树的前序遍历
# Definition for a binary tree node.
import collections
from typing import List, Optional


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.val)


class Solution:

	# 前序
	def preorderTraversal(self, root: TreeNode) -> List[int]:
		if not root:
			return []

		left = self.preorderTraversal(root.left)
		right = self.preorderTraversal(root.right)

		print([root.val] + left + right)
		return [root.val] + left + right

	def preorderTraversalByIterate(self, root: TreeNode) -> List[int]:
		# 根结点为空则返回空列表
		if not root:
			return []
		stack = [root]
		result = []
		while stack:
			node = stack.pop()
			# 中结点先处理
			result.append(node.val)
			# 右孩子先入栈
			if node.right:
				stack.append(node.right)
			# 左孩子后入栈
			if node.left:
				stack.append(node.left)
		return result

	# 迭代法的统一书写
	def preorderTraversalUnity(self, root: TreeNode) -> List[int]:
		result = []
		st = []
		if root:
			st.append(root)
		while st:
			node = st.pop()
			if node != None:
				if node.right:  # 右
					st.append(node.right)
				if node.left:  # 左
					st.append(node.left)
				st.append(node)  # 中
				st.append(None)
			else:
				node = st.pop()
				result.append(node.val)
			print([node.val if node else None for node in st])  # 打印出st中每个TreeNode的val值
			print("result" + str(result))
		return result

	# 中序
	def inorderTraversal(self, root: TreeNode) -> List[int]:
		if not root:
			return []

		left = self.inorderTraversal(root.left)
		right = self.inorderTraversal(root.right)

		return left + [root.val] + right

	def inorderTraversalByInterate(self, root: TreeNode) -> List[int]:
		if not root:
			return []
		stack = []  # 不能提前将root结点加入stack中
		result = []
		cur = root
		while cur or stack:
			# 先迭代访问最底层的左子树结点
			if cur:
				stack.append(cur)
				cur = cur.left
			# 到达最左结点后处理栈顶结点
			else:
				cur = stack.pop()
				result.append(cur.val)
				# 取栈顶元素右结点
				cur = cur.right
		return result

	def postorderTraversal(self, root: TreeNode) -> List[int]:
		if not root:
			return []

		left = self.postorderTraversal(root.left)
		right = self.postorderTraversal(root.right)

		return left + right + [root.val]

	# 和前序遍历反转一下
	def postorderTraversalByIterate(self, root: TreeNode):
		# 根结点为空则返回空列表
		if not root:
			return []
		stack = [root]
		result = []
		while stack:
			node = stack.pop()
			# 中结点先处理
			result.append(node.val)
			# 右孩子先入栈
			if node.left:
				stack.append(node.left)
			# 左孩子后入栈
			if node.right:
				stack.append(node.right)
		return result[::-1]

	# 广度优先遍历 层数遍历  利用长度法 ------------------------------------------
	def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
		if not root:
			return []
		queue = collections.deque([root])
		result = []
		while queue:
			level = []
			print("len : " + str(len(queue)))
			for i in range(len(queue)):
				print("No. " + str(i + 1))
				print([node.val if node else None for node in queue])
				cur = queue.popleft()
				level.append(cur.val)
				if cur.left:
					queue.append(cur.left)
				if cur.right:
					queue.append(cur.right)

				print("下一次 :")
				print([node.val if node else None for node in queue])
			result.append(level)
			print("result: ")
			print(result)
			print()
		return result

	# -----------------------------------------------------------------------

	def levelOrder1(self, root: Optional[TreeNode]) -> List[List[int]]:
		levels = []
		self.helper(root, 0, levels)
		return levels

	def helper(self, node, level, levels):
		if not node:
			return
		if len(levels) == level:
			levels.append([])
		levels[level].append(node.val)
		self.helper(node.left, level + 1, levels)
		self.helper(node.right, level + 1, levels)

	# 自己编写递归调用
	def level_order2(self, root: Optional[TreeNode]) -> List[int]:
		if not root:
			return []

		def bfs(node, level, result):
			print("result :", result)
			if len(result) == level:
				result.append([])
				print("result added :", result)
			result[level].append(node.val)
			if node.left:
				bfs(node.left, level + 1, result)
			if node.right:
				bfs(node.right, level + 1, result)

		result = []
		bfs(root, 0, result)
		# Flatten the list of lists into a single list
		return [sublist for sublist in result]


if __name__ == '__main__':
	# 创建树的节点
	root = TreeNode(1)
	node1 = TreeNode(2)
	node2 = TreeNode(3)
	node3 = TreeNode(4)
	node4 = TreeNode(5)
	node5 = TreeNode(6)
	node6 = TreeNode(7)

	# 构建树的结构
	root.left = node1
	root.right = node2
	node1.left = node3
	node1.right = node4
	node2.left = node5
	node2.right = node6

	# Solution().levelOrder(root)
	print(Solution().level_order2(root))

"""
        1
      /   \
     2     3
   /  \
 4     5      
"""
