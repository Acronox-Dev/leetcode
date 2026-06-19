class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        height = 0
        max = 0
        for i in range(len(gain)) :
            height += gain[i]
            if height > max :
                max = height
        return max