class Solution:
    def canJumpRecursive(self, nums: List[int], i: int, data) -> bool :
        if i >= len(nums) - 1 : return True

        for j in range(1,nums[i] + 1):
            if not((i+j) in data) :
                data[(i+j)] = self.canJumpRecursive(nums,i+j, data)
            if data[(i+j)] :
                return True
        return False

    def canJump(self, nums: List[int]) -> bool:
        if nums == [] :
            return False
        data = {}
        return self.canJumpRecursive(nums,0,data)