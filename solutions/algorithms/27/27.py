class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)

        for j in range(n):
            num = nums[j]
            if num != val :
                nums[i] = num
                i += 1

        return i