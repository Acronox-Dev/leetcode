# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbersWithCarry(self, l1: Optional[ListNode], l2: Optional[ListNode], carry = 0) -> Optional[ListNode]:
        if (not l1 and not l2) :
            if carry == 0 :
                return None
            else :
                return ListNode(carry,None)

        val1 = 0
        val2 = 0
        next1 = None
        next2 = None

        if l1 : 
            val1 = l1.val
            next1 = l1.next
        if l2 : 
            val2 = l2.val
            next2 = l2.next

        val = val1 + val2 + carry
        digit = val % 10
        next_carry = val // 10

        next = self.addTwoNumbersWithCarry(next1, next2, next_carry) 
        
        return ListNode(digit, next)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.addTwoNumbersWithCarry(l1, l2)