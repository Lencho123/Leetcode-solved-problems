class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix),len(matrix[0])
        res = 0
        
        for r in range(row):
            for c in range(col):
                left = matrix[r][c-1] if c > 0 else 0
                top = matrix[r-1][c] if r > 0 else 0
                diag = matrix[r-1][c-1] if r > 0 and c > 0 else 0
                
                if matrix[r][c] != 0:
                    matrix[r][c]+=min(left,top,diag)
                    
                res+=matrix[r][c]
        return res