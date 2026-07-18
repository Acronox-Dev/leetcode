class Solution:
    # Rabin-Karp algorithm
    def strStr(self, haystack: str, needle: str) -> int:
        # Initialization
        n = len(needle)
        h = len(haystack)
        
        # Base Case
        if n > h : return -1

        # Needle Hash
        n_hash = sum([ord(needle[i]) for i in range(n)])

        # Find needle in haystack
        hash = sum([ord(haystack[i]) for i in range(n)])

        for i in range(h - n + 1) :
            if hash == n_hash and needle == haystack[i : i + n] :
                return i
            if i < h - n:
                hash = hash - ord(haystack[i]) + ord(haystack[i + n])
            
        return -1