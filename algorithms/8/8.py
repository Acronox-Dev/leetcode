ascii_to_digit = {
    "0" : 0, 
    "1" : 1, 
    "2" : 2, 
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9
}

class Solution:
    def isDigit(self, c):
        return c in ascii_to_digit.keys()
    
    def charToDigit(self, c):
        return ascii_to_digit[c]

    def myAtoi(self, s: str) -> int:
        result = 0
        i = 0
        n = len(s)

        # Skip leading whitespace
        while(i < n and s[i] == " ") : 
            i += 1

        # Find the sign
        sign = 1

        if i < n and s[i] == "+" :
            i += 1
        elif i < n and s[i] == "-" :
            sign = -1
            i += 1

        # Convert the string into an integer
        leadingZeros = True
        while(i < n) :
            if leadingZeros and s[i] == "0" :
                i += 1
            elif leadingZeros :
                leadingZeros = False
            else :
                if self.isDigit(s[i]): 
                    digit = self.charToDigit(s[i])
                    result = result * 10 + digit
                    i += 1
                else :
                    break
        
        result = result * sign

        # Rounding
        power_two = 2 ** 31
        if result >= power_two - 1 :
            result = power_two - 1
        elif result <= -1 * power_two :
            result = -1 * power_two
        
        return result