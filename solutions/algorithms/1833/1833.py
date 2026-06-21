class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        n = len(costs)

        # Base Case
        if coins < costs[0] : return 0

        # General Case
        i = 0

        while(coins >= 0 and i < n) :
            c = costs[i]
            coins -= c
            if coins >= 0 : 
                i += 1

        return i
    

s = Solution()
s.maxIceCream([1,3,2,4,1],7)