class Solution:
    def maxArea(self, height: List[int]) -> int:
        heightDistance = []
        n = len(height)

        for i in range(n):
            heightDistance.append(i * height[i])

            