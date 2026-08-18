class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        result = ""
        carry = 0

        while(i >= 0 or j >= 0 or carry != 0) :
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0

            temp = digit1 + digit2 + carry
            sum = temp % 10
            carry = temp // 10

            result = str(sum) + result
            i -= 1
            j -= 1

        return result
