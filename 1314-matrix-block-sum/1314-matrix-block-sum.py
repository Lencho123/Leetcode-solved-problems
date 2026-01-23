class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        row,col = len(mat),len(mat[0])
        
        presum = [[0]*col for i in range(row)]
        
        
        for r in range(row):
            for c in range(col):
                top = presum[r-1][c] if r-1 >= 0 else 0
                left = presum[r][c-1] if c-1 >= 0 else 0
                diag = presum[r-1][c-1] if r-1 >= 0 and c-1 >= 0 else 0
                
                presum[r][c] = top + left - diag + mat[r][c]
            
        for r in range(row):
            for c in range(col):
                ro,co = max(0, r-k),max(0,c-k)
                rf,cf = min(row-1,r+k), min(col-1,c+k)
                
                top = presum[ro-1][cf] if ro-1 >= 0 else 0
                left = presum[rf][co-1] if co-1 >= 0 else 0
                diag = presum[ro-1][co-1] if ro-1 >= 0 and co-1 >= 0 else 0
                
                mat[r][c] = presum[rf][cf] - top - left + diag
        return mat
                