"""
二叉树方法合集
          1
         / \
        2   3
           / \
          4   5
			 /
			6
"""
from collections import deque
from typing import List


class TreeNode(object):
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right




class Solutions(object):
	# 深度优先 递归方式  三种遍历只需要交换位置即可
	def preorderTraversal(self, root: TreeNode) -> List[int]:
		if not root:
			return []

		left = self.preorderTraversal(root.left)
		right = self.preorderTraversal(root.right)

		print([root.val] + left + right)
		return [root.val] + left + right

	# 深度优先  迭代法  使用栈  前序遍历  中左右
	def preorderTraversalByStack1(self, root: TreeNode) -> List[int]:
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
		return result

	# 广度优先 层序遍历 使用迭代的方式
	def levelOrderTraversal11(self, root: TreeNode) -> List[int]:
		if not root:
			return []
		result = []
		queue = deque([root])
		while queue:
			que_len = len(queue)
			for _ in range(que_len):
				node = queue.popleft()
				result.append(node.val)
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)
		return result







	# 使用队列  前序遍历 中左右  前序遍历
	def preorderTraversalByQueue1(self, root: TreeNode) -> List[int]:
		result = []
		q = deque()
		if root:
			q.append(root)
		while q:
			node = q.popleft()  # 从队列前端取出节点
			if node:
				result.append(node.val)  # 访问当前节点
				if node.left:  # 如果有左孩子，左孩子先入队
					q.append(node.left)
				if node.right:  # 如果有右孩子，右孩子后入队
					q.append(node.right)
			print(result)
		return result

	# 中序遍历 使用栈
	def preorderTraversalByStack2(self, root: TreeNode) -> List[int]:
		result = []
		st = []
		if root:
			st.append(root)
		while st:
			node = st.pop()
			if node != None:
				if node.right:  # 右
					st.append(node.right)
				st.append(node)  # 中
				st.append(None)
				if node.left:  # 左
					st.append(node.left)
			else:
				node = st.pop()
				result.append(node.val)
			print(result)

		return result

	# 中序遍历 使用队列
	def preorderTraversalByQueue2(self, root: TreeNode) -> List[int]:
		result = []
		queue = deque()
		current = root
		while current or queue:
			while current:
				queue.append(current)
				current = current.left
			current = queue.pop()
			result.append(current.val)
			current = current.right
			print([node.val if node else None for node in queue])
			print(result)
			print()

		return result

	# 后序遍历 使用队列
	def postorderTraversalByQueue(self, root: TreeNode) -> List[int]:
		result = []
		stack = deque()
		last_visited = None

		while stack or root:
			while root:
				stack.append(root)
				root = root.left
			peek_node = stack[-1]
			if peek_node.right and last_visited != peek_node.right:
				root = peek_node.right
			else:
				stack.pop()
				result.append(peek_node.val)
				last_visited = peek_node

		return result




if __name__ == '__main__':
	# 创建叶子节点
	left_child = TreeNode(val=4)
	right_child = TreeNode(val=5)

	# 创建第二层的左右节点
	left = TreeNode(val=2, left=left_child)
	right = TreeNode(val=3, right=right_child)

	# 创建根节点，并将第二层的左右节点连接到根节点
	root = TreeNode(val=1, left=left, right=right)

	# 添加更多节点来增加复杂性
	left_left_child = TreeNode(val=6)
	left_right_child = TreeNode(val=7)
	right_left_child = TreeNode(val=8)
	right_right_child = TreeNode(val=9)

	# 连接新的节点
	left.left.left = left_left_child
	left.left.right = left_right_child
	left_right_child.right = right_left_child
	right_child.right = right_right_child

	print(Solutions().preorderTraversalByStack1(root))
	print(Solutions().levelOrderTraversal11(root))
