class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])

        presum = [[0]*col for i in range(row)]
        
        for r in range(row):
            for c in range(col):
                above = presum[r-1][c] if r-1 >= 0 else 0
                left = presum[r][c-1] if c-1 >= 0 else 0
                diag = presum[r-1][c-1] if c-1 >= 0 and r-1 >= 0 else 0

                presum[r][c] = above + left - diag + grid[r][c]

        def is_magic(r,c,side):
            diag1,diag2 = 0,0
            for i in range(side):
                diag1+=grid[r+i][c+i]
                diag2+=grid[r+i][c+side-i-1]
            
            if diag1 != diag2:
                return False

            # check all rows and cols magicity
            for i in range(side):
                # rows magicity check
                if diag1 != checksum(r+i,c, r+i,c+side-1):
                    return False
                # cols magicity check
                if  diag1 != checksum(r,c+i,r+side-1,c+i):
                    return False
            return True

        
        def checksum(r,c,rf,cf):
            total = presum[rf][cf] 
            left = presum[rf][c-1] if c-1 >= 0 else 0
            top = presum[r-1][cf] if r-1 >= 0 else 0
            diag = presum[r-1][c-1] if r-1 >= 0 and c-1 >= 0 else 0

            return total - left - top + diag
        
        res = 1
        for r in range(row):
            for c in range(col):
                side = min(row-r,col-c)+1
                for s in range(side):
                    if is_magic(r,c,s):
                        res = max(res,s)
        return res
                