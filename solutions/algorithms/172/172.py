data = {0 : (0,0)}

class Solution:
    def count_power_m(self, n: int, m: int) :
        count = 0
        while(n % m == 0) :
            n = n // m
            count += 1
        return count

    def count_2_5(self, n: int, n2: int, n5: int) :
        if n == 0 : return (n2,n5)

        if not(n in data.keys()) :
            n2,n5 = self.count_2_5(n-1,n2,n5)
            n2 += self.count_power_m(n,2)
            n5 += self.count_power_m(n,5)
            data[n] = (n2,n5)

        return data[n]

    def trailingZeroes(self, n: int) -> int:
        n2,n5 = self.count_2_5(n,0,0)
        return min(n2,n5)