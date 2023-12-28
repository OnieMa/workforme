from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        # 定义两个指针
        slow = head
        fast = head

        while fast and fast.next:

            # fast每次走2步 slow每次走一步 相对slow来讲, fast每次都比slow多走一步 , 所以如果在环内 fast一定会与slow相遇
            slow = slow.next
            fast = fast.next.next

            # 如果两个节点相遇 则将slow放置链表开头  两个指针每次均进行1步 再相遇时 slow所在的节点 就是环的起点
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

    def detectCycle(self, head: ListNode) -> ListNode:

        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
