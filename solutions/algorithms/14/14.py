class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)

        # Base Cases
        if n == 0 : return ""
        if n == 1 : return strs[0]

        # Loop
        prefix = strs[0]
        p = len(prefix)
        i = 1

        while(i < n) :
            current = strs[i]
            m = len(current)

            j = 0
            while(j < m and j < p and current[j] == prefix[j]) :
                j += 1
            p = min(p,j)
            i += 1

        return prefix[:p]

