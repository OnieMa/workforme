from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(head: Optional[ListNode]):
    nums = []
    nums.append(head.val)

    while head.next:
        nums.append(head.next.val)
        head = head.next
    print(nums)