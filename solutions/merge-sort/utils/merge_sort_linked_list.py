# Merge Sort Linked List

from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    # Find the middle
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    left = head
    right = slow.next
    slow.next = None

    # Recursive sort
    left_sorted = sortList(left)
    right_sorted = sortList(right)

    # Merge
    dummy = ListNode(0)
    temp = dummy
    while left_sorted and right_sorted:
        if left_sorted.val <= right_sorted.val:
            temp.next = left_sorted
            left_sorted = left_sorted.next
        else:
            temp.next = right_sorted
            right_sorted = right_sorted.next
        temp = temp.next

    temp.next = left_sorted or right_sorted
    return dummy.next