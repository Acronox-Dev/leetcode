class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s : return 0
        
        subString = ""
        maxLength = 0

        for i in range(len(s)) :
            while(s[i] in subString):
                subString = subString[1:]
            subString += s[i]

            n = len(subString)
            if (n > maxLength) :
                maxLength = n
        
        return maxLength