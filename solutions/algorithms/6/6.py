class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows == 1) : return s

        stringRows = ["" for i in range(numRows)]

        k = 0
        decrement = False

        for i in range(len(s)) :
            stringRows[k] += s[i]
            
            if decrement :
                k -= 1
                decrement = False if (k == 0) else True
            else :
                k += 1
                decrement = True if (k >= (numRows - 1)) else False

        return "".join(stringRows)

            
