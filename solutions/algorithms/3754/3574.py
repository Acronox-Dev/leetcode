class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # Find x and the sum of its digits
        sum = 0
        x = 0
        pow = 1
        
        while(n != 0) :
            d = n % 10
            
            if d != 0 :
                sum += d
                x += pow * d
                pow *= 10

            n = n // 10

        return x * sum