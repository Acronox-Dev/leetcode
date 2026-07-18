class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        length = 0
        i = n - 1

        # Skip ending space characters
        while(i >= 0 and s[i] == ' ') : 
            i -= 1

        # Find length of last word
        while(i >= 0 and s[i] != ' ') :
            i -= 1
            length += 1

        return length