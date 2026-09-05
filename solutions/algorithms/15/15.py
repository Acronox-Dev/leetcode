class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Convert to a hashmap
        n = len(nums)
        existence = {}
        for i in range(n):
            existence[nums[i]] = i

        # Loop to get the triplets
        res = set()
        for i in range(n):
            for j in range(i + 1, n):
                x = nums[i]
                y = nums[j]
                target = -x - y
                if target in existence:
                    k = existence[target]
                    if k > j: 
                        triplet = tuple(sorted([x, y, target]))
                        res.add(triplet)

        return [list(t) for t in res]