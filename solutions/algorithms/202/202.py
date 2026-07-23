data = {0 : False, 1 : True, 2 : False}

class Solution:
    def isHappy(self, n: int) -> bool:
        if not(n in data) :
            data[n] = False

            next_number = 0
            temp = n
            while(temp > 0) :
                d = temp % 10
                next_number += d * d
                temp = temp // 10

            data[n] = self.isHappy(next_number)
        return data[n]