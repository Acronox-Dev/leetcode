class Solution:
    def isPalindrome(self, s: str) -> bool :
        if not s : return True

        n = len(s)
        for i in range(n//2):
            if(s[i] != s[n - i - 1]) :
                return False
        
        return True

    def longestPalindrome(self, s: str) -> str:
        if not s : return ""
        
        subString = ""
        bestString = ""
        maxLength = 0

        for i in range(len(s)) :
            subString = s[:(i+1)]
            while(not self.isPalindrome(subString)) :
                subString = subString[1:]
            
            n = len(subString)
            if n > maxLength :
                maxLength = n
                bestString = subString
        
        return bestString