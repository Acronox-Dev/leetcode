class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Move values to their ideal index (so that nums[i] = i + 1)
        i = 0
        while(i < n) :
            v = nums[i]

            if v != i + 1 and 1 <= v and v <= n and nums[v-1] != v :
                nums[i] = nums[v - 1]
                nums[v - 1] = v
            else :
                i += 1

        # Find the missing value
        for i in range(n):
            if nums[i] != i + 1 :
                return i + 1
        
        return n + 1