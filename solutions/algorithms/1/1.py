class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Convert to a hashmap
        n = len(nums)
        existence = {}
        for i in range(n) :
            existence[nums[i]] = i

        # Fix one value and search for the other
        res = []
        for i in range(n):
            x = nums[i]
            if target - x in existence:
                j = existence[target - x]
                if i != j : 
                    res.append(i)
                    res.append(j)
                    break

        return res