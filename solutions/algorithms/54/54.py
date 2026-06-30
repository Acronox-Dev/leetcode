class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix : return []

        # Constants
        m = len(matrix)
        n = len(matrix[0])

        # Util Function to get the kth Ring values
        def getRing(k : int) :
            ring = []
            i = k
            j = k
            l1 = m - 2 * k
            l2 = n - 2 * k
            
            # Right
            while(j < n - k) :
                ring.append(matrix[i][j])
                j += 1
            j -= 1
            i += 1

            # Bottom
            while(i < m - k) :
                ring.append(matrix[i][j])
                i += 1
            i -= 1
            j -= 1
            
            # Left
            if l1 != 1 and l2 != 1 :
                while(j >= k) :
                    ring.append(matrix[i][j])
                    j -= 1
                j += 1
                i -= 1

            # Up
                while(i >= k) :
                    ring.append(matrix[i][j])
                    i -= 1

            if l1 != 1 and l2 != 1 :
                ring.pop()
            return ring
        
        # Result
        result = []
        d = (min(m, n) + 1) // 2

        for k in range(d) :
            ring = getRing(k)
            for r in ring :
                result.append(r)

        return result