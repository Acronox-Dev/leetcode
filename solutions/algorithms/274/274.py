class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Initialization
        n = len(citations)
        count = [0 for i in range(n)]
        h = 0

        # Loop
        for i in range(n) :
            v = citations[i]
            d = min(v,n)
            for k in range(d) :
                count[d - 1 - k] += 1
                if count[d - 1 - k] >= d - k and h < d - k :
                    h = d - k

        return h