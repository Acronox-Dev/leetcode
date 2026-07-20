class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def aux(start : int, end : int) :
            if start > end : return start

            m = (start + end) // 2
            if nums[m] == target : return m
            if target < nums[m] : return aux(start, m - 1)
            return aux(m + 1, end)

        return aux(0, len(nums) - 1)