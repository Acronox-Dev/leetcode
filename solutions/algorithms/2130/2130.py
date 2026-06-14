# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Convert the Linked List into an Array and then find the max twin sum
    def pairSum(self, head: Optional[ListNode]) -> int:
        array = []
        while(head) :
            val = head.val
            array.append(val)
            head = head.next

        n = len(array)
        max = 0
        for i in range(n//2) :
            sum = array[i] + array[n - i - 1]
            if sum > max :
                max = sum
        return max