from typing import Optional, List

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

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == [] or lists == [None] : return None

        while len(lists) > 1 :
            mergedLists = []
            for i in range(0, len(lists), 2) :
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.merge(l1, l2))
            lists = mergedLists

        return lists[0]
        
    