from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        temp = dummy

        while(left and right) :
            if left.val <= right.val :
                temp.next = left
                temp = temp.next
                left = left.next
            else :
                temp.next = right
                temp = temp.next
                right = right.next

        temp.next = left or right

        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next : return head

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

        left = head
        right = slow.next
        slow.next = None

        return self.merge(self.sortList(left),self.sortList(right))