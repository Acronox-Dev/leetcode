data = {1 : 1, 2 : 2}

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2 : return data[n]

        if not ((n-1) in data) :
            data[n-1] = self.climbStairs(n-1)
        if not ((n-2) in data) :
            data[n-2] = self.climbStairs(n-2)

        return data[n-1] + data[n-2]