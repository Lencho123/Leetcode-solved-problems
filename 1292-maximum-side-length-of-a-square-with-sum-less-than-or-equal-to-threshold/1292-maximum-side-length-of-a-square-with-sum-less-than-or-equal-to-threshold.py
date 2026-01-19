class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        row,col = len(mat),len(mat[0])
        presum = [[0]*col for i in range(row)]

        for r in range(row):
            for c in range(col):
                top = presum[r-1][c] if r-1 >= 0 else 0
                left = presum[r][c-1] if c-1 >= 0 else 0
                diag = presum[r-1][c-1] if r-1 >= 0 and c-1 >= 0 else 0
                presum[r][c] = top + left - diag + mat[r][c]
        
        res = 0
        for r in range(row):
            for c in range(col):
                side = min(row-r,col-c)
                for s in range(side):
                    rf,cf = r+s, c+s
                    total = presum[rf][cf]
                    top = presum[r-1][cf] if r-1 >= 0 else 0
                    left = presum[rf][c-1] if c-1 >= 0 else 0
                    diag = presum[r-1][c-1] if c-1 >= 0 and r-1 >= 0 else 0

                    net_val = total - top - left + diag
                    if net_val <= threshold:
                        res = max(res,s+1)
        return res