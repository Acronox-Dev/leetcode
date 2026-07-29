class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        data = [[-1 for _ in range(2)] for _ in range(n)]
        
        def aux(index: int, holding: int) -> int:
            if index >= n: return 0
            if data[index][holding] != -1: return data[index][holding]

            do_nothing = aux(index + 1, holding)
            
            if holding:
                do_something = prices[index] + aux(index + 1, 0)
            else:
                do_something = -prices[index] + aux(index + 1, 1)
                
            data[index][holding] = max(do_nothing, do_something)
            return data[index][holding]
            
        return aux(0, 0)