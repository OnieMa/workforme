from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = dummy
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return cur.next





    def removeElements1(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 创建虚拟头部节点以简化删除过程
        dummy_head = ListNode(next=head)

        # 遍历列表并删除值为val的节点
        current = dummy_head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy_head.next


"""
  while(head!=null && head.val==val){
        head = head.next;
    }
    ListNode curr = head;
    while(curr!=null){
        while(curr.next!=null && curr.next.val == val){
            curr.next = curr.next.next;
        }
        curr = curr.next;
    }
    return head;

    # 不使用虚拟节点
"""


# 错误写法
def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    while head is not None and head.val == val:
        head = head.next

    # 遍历列表并删除值为val的节点
    current = head
    while current.next:
        if current.next.val == val:
            current.next = current.next.next
        current = current.next
    return head


def removeElements1(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    # 首先移除头部是目标值的节点
    while head is not None and head.val == val:
        head = head.next
    print_list(head)
    # 现在头部节点不是目标值，开始遍历链表的其余部分
    current = head
    while current is not None and current.next is not None:
        if current.next.val == val:
            current.next = current.next.next  # 移除下一个节点
        else:
            current = current.next  # 只有当下一个节点不需要移除时，当前节点才移动
        print_list(current)
    print_list(head)
    return head  # 返回新的头节点


def print_list(head: Optional[ListNode]):
    nums = []
    nums.append(head.val)

    while head.next:
        nums.append(head.next.val)
        head = head.next
    print(nums)


if __name__ == '__main__':
    head = None
    for i in range(6, 0, -1):
        head = ListNode(i, head)



    removeElements1(head, 4)
