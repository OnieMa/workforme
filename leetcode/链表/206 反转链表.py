from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = None
        fast = head
        while (fast != None):
            temp = fast.next
            fast.next = slow
            slow = fast
            fast = temp

        return slow

    # 反转 11.20
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = None
        fast = head
        while fast:
            temp = fast.next
            fast.next = slow
            slow = fast
            fast = temp
