class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row,col = len(matrix),len(matrix[0])
        
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    matrix[r][c] = "0"
                    
                    for i in range(row):
                        matrix[i][c] = "0" if matrix[i][c] != 0 else 0
                    
                    for j in range(col):
                        matrix[r][j] = "0" if matrix[r][j] != 0 else 0
                        
        for r in range(row):
            for c in range(col):
                matrix[r][c] = int(matrix[r][c])