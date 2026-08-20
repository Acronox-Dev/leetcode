class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        # 1 .Find the indexes of the rows and cols to modify
        rows = [False for i in range(m)]
        cols = [False for j in range(n)]

        for i in range(m) :
            for j in range(n) :
                if matrix[i][j] == 0 :
                    rows[i] = True
                    cols[j] = True

        # 2. Set zeros
        for i in range(m) :
            if rows[i] :
                for k in range(n) :
                    matrix[i][k] = 0

        for j in range(n) :
            if cols[j] :
                for k in range(m) :
                    matrix[k][j] = 0