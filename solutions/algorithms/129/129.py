# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root : return 0

        numbers = []
        def aux(root : Optional[TreeNode], current_number: int) :
            if not root : numbers.append(current_number)

            current_number = current_number * 10 + root.val

            if not root.left and not root.right : numbers.append(current_number)
            if root.left : aux(root.left, current_number)
            if root.right : aux(root.right, current_number)

        aux(root, 0)

        return sum(numbers)