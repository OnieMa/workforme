from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        cur = dummy_head

        while cur.next and cur.next.next:
            temp = cur.next
            cur.next = cur.next.next
            next_node = cur.next.next
            temp.next = next_node
            cur.next.next = temp

            cur = cur.next.next

        return dummy_head.next

    # 11.20
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = dummy
        while cur.next and cur.next.next:
            temp = cur.next
            cur.next = cur.next.next
            real_next = cur.next.next
            cur.next.next = temp
            temp.next = real_next

            cur = cur.next.next
        return dummy.next
