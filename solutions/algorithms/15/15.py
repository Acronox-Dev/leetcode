class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Convert to a hashmap
        n = len(nums)
        existence = {}
        for i in range(n) :
            existence[nums[i]] = i

        # Loop to get the triplets
        res = []
        for i in range(n) :
            for j in range(i+1, n) :
                x = nums[i]
                y = nums[j]
                if -x-y in existence:
                    k = existence[-x-y]
                    if k > j : 
                        res.append([x,y,-x-y])

        return res