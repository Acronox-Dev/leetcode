# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head : return None

        temp = head
        before = None
        middle = head
        after = head.next
        shift = False

        while(temp) :
            temp = temp.next

            if shift :
                before = middle
                middle = after
                after = after.next

            shift = not shift

        if before :
            before.next = after
        else :
            head = None

        return head
