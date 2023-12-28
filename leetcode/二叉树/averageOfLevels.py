from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children

class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def averageOfLevels(self, root):
        if not root:
            return []
        qu = deque([root])
        result = []
        while qu:
            level = []
            qu_len = len(qu)
            for _ in range(0, qu_len):
                node = qu.popleft()
                level.append(node.val)
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)
            sum = 0
            for i in range(len(level)):
                sum += level[i]

            result.append(sum / len(level))

        return result

    # n叉树
    def levelOrder(self, root):
        if not root: return []
        result = []
        qu = deque([root])
        while qu:
            level = []
            qu_len = len(qu)

            # 遍历这一层的每一个节点
            for _ in range(0, qu_len):
                node = qu.popleft()
                level.append(node.val)

                for child in node.children:
                    qu.append(child)

            result.append(level)  # 这一层的所有节点的值 放在一个[]中
        return result

    def largestValues(self, root):
        if not root: return []
        queue = deque([root])
        result = []
        while queue:
            max_value = float('-inf')
            for _ in range(len(queue)):
                node = queue.popleft()
                max_value = max(max_value, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(max_value)
        return result

    def connect(self, root):
        if not root:
            return None
        queue = deque([root])
        while queue:
            preNode = None
            print([qu.val for qu in queue])
            qu_size = len(queue)
            for i in range(0, qu_size):
                curNode = queue.popleft()
                if preNode:
                    preNode.next = curNode
                preNode = curNode
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
            print([qu.val for qu in queue])
            print()
        return root

    def maxDepth(self, root):
        if not root:
            return 0
        depth = 0
        queue = deque([])


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

    Solution().connect(root)
