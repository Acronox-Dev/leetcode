class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialization
        n = len(height)
        p1 = 0
        p2 = n - 1
        max = 0

        # Loop
        while(p1 < p2) :
            v1, v2 = height[p1], height[p2]

            temp = min(v1,v2) * (p2 - p1)
            if temp > max : max = temp
            
            if v2 > v1 : p1 += 1
            else : p2 -= 1

        return max


            