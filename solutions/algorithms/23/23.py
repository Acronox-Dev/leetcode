# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == [] or lists == [None] : return None

        list1 = lists[0]
        i = 1
        n = len(lists)

        while(i < n) :
            list2 = lists[i]

            # Merge list1 and list2, choosing the lowest value
            l1 = list1 
            l2 = list2 
            temp = ListNode(0,None)
            result = temp
 
            while(l1 and l2) :
                v1 = l1.val
                v2 = l2.val
                
                if v1 <= v2 :
                    v = v1
                    l1 = l1.next
                else :
                    v = v2
                    l2 = l2.next

                temp.next = ListNode(v,None)
                temp = temp.next

            # Add remaining values from one of the lists
            while(l1) :
                temp.next = ListNode(l1.val,None)
                temp = temp.next
                l1 = l1.next
            while(l2) :
                temp.next = ListNode(l2.val,None)
                temp = temp.next
                l2 = l2.next

            # Update
            list1 = result.next
            if list2 :
                list2 = list2.next
            i += 1

        return list1
    