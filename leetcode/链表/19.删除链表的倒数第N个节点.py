from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


#  dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
#      |              |
#                     |              |

class Solution:

    def removeNthFromEnd1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        slow, fast = dummy_head, dummy_head  # 让两个指针都指向虚拟节点

        # 先让fast向前n+1步
        for i in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy_head.next

    # 11.20
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        slow, fast = dummy_head, dummy_head  # 让两个指针都指向虚拟节点
        # 先让fast前进n步
        for _ in range(n):
            fast = fast.next

        # 让fast移动到最后一个元素
        while fast.next:
            fast = fast.next
            slow = slow.next

        # 这时候 slow所指的元素的下一个元素就是被删除的元素
        slow.next = slow.next.next

        return dummy_head.next
