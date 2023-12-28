class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # 11.20
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        b = headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        size_a, size_b = 0, 0

        # 分别求 a b 的长度
        cur = headA
        while cur:
            cur = cur.next
            size_a += 1
        cur = headB
        while cur:
            cur = cur.next
            size_b += 1

        curA, curB = headA, headB
        # 让A的长度一直大于B
        if size_b > size_a:
            size_a, size_b = size_b, size_a
            curA, curB = curB, curA

        # 让A的尾部和B对齐 那么头需要移动 长度差
        for i in range(size_a - size_b):
            curA = curA.next

        while curA:
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next
        return None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 网上大神写法

class Solution1:
    """
    这段代码是用来找到两个单向链表（单链表）相交的起始节点的。链表A的头节点是`headA`，链表B的头节点是`headB`。代码中定义了一个名为`Solution`的类，其中包含了名为`getIntersectionNode`的方法。这个方法接受两个链表的头节点作为参数，并返回它们相交的起始节点。如果两个链表不相交，则返回`None`。

    以下是该方法的思路：

    1. 初始化两个指针`a`和`b`，分别指向链表A和链表B的头节点。

    2. 同时遍历两个链表，`a`指针通过链表A移动，`b`指针通过链表B移动。

    3. 如果某个指针到达链表的末尾（即变为`None`），则将该指针移到另一个链表的头节点。这意味着：
       - 如果`a`指针到达链表A的末尾，它会跳转到链表B的头节点。
       - 如果`b`指针到达链表B的末尾，它会跳转到链表A的头节点。

    4. 继续遍历，直到两个指针`a`和`b`相遇（即`a == b`），或者两者都到达各自链表的末尾而变为`None`。

    5. 如果两个链表相交，那么这两个指针最终会在相交节点相遇，并返回该相交节点。如果不相交，两个指针都会到达各自链表的末尾并同时变为`None`，此时函数返回`None`。

    为什么这个算法能够找到相交节点呢？考虑以下情况：

    - 如果两个链表长度相同且相交，那么两个指针会在第一次遍历时在相交点相遇。
    - 如果两个链表长度不同且相交，那么第一次遍历时两个指针不会在相交点相遇。但是，当一个指针移到另一个链表的头节点后，两个指针会走过相同长度的路径（即两个链表的总长度），因此在第二次遍历时，它们会在相交节点相遇。

    这种方法有效地消除了两个链表长度差异的影响，使得两个指针能够在相交节点相遇。这个解决方案不需要额外的存储空间，且时间复杂度为O(m+n)，其中m和n分别是两个链表的长度。
    """

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A

    """
    如果链表A为空，那么我们的指针`a`初始化为`None`。如果链表B不为空，那么指针`b`将指向链表B的头节点`headB`。
    
    在循环中，我们会检查`a`和`b`是否相等。在第一次迭代时，`a`是`None`，而`b`是链表B的头节点，因此`a != b`。
    
    然后按照算法逻辑：
    
    - 因为`a`是`None`，所以它会被设置为`headB`（链表B的头节点）。
    - `b`如果不是`None`，就会移动到下一个节点，如果是`None`，则会被设置为`headA`（但在这个案例中`headA`是`None`）。
    
    在这一轮循环结束后，`a`指向了链表B的头节点，而`b`指向了链表B的第二个节点（如果链表B只有一个节点，则`b`会变为`None`）。
    
    接下来的情况是：
    
    - `a`将继续遍历链表B，直到到达末尾并变为`None`。
    - `b`也将遍历链表B，但由于它比`a`领先一步，所以它将先到达末尾并变为`None`。
    
    在某一点，`b`到达链表B的末尾并变为`None`。在下一次迭代中，`b`会被设置为`headA`（也是`None`）。在这之后，两个指针`a`和`b`都会是`None`，因为：
    
    - `a`在遍历完链表B后变为`None`。
    - `b`在到达链表B末尾变为`None`后，下一步被设置为`headA`，也是`None`。
    
    此时，`a == b`（因为它们都是`None`），循环结束，算法返回`None`，表示链表不相交。
    
    总结：算法确保了即使一个链表为空，两个指针也会在某一点同时为`None`，从而结束循环并返回正确的结果。
    """
