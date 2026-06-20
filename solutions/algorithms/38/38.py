data = ["", "1"]
length = 2

class Solution:
    def transformation(self, s: str) -> str:
        result = ""
        n = len(s)
        i = 0
        count = 1

        while(i < n) :
            while(i < n - 1 and s[i] == s[i + 1]) :
                count  += 1
                i += 1
            result += str(count) + s[i]
            count = 1
            i += 1

        return result

    def countAndSay(self, n: int) -> str:
        global length, data

        if n >= length :
            s = data[length - 1]

            while(length <= n) :
                s = self.transformation(s)
                data.append(s)
                length += 1

        return data[n]
