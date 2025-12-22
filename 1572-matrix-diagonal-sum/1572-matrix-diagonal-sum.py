class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        diag_sum = 0
        for i in range(n):
            for j in range(n):
                if i == j or i+j == n-1:
                    diag_sum+=mat[i][j]
        return diag_sum