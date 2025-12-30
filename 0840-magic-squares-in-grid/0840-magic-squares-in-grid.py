class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])

        def is_magic(r,c):
            sm = grid[r][c]+grid[r][c+1]+grid[r][c+2]
            if sm != grid[r+1][c] + grid[r+1][c+1]+grid[r+1][c+2] or sm != grid[r+2][c] + grid[r+2][c+1]+grid[r+2][c+2] or sm != grid[r][c] + grid[r+1][c] + grid[r+2][c] or sm != grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] or sm != grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] or sm != grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] or sm != grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c]:
                return False
        
            distnict = set()
            for i in range(r, r+3):
                for j in range(c,c+3):
                    if grid[i][j] > 9 or grid[i][j] <= 0:
                        print(grid[i][j])
                        return False
                    distnict.add(grid[i][j])
            if len(distnict) != 9:
                return False
            return True
            
        res = 0
        
        for r in range(row):
            for c in range(col):
                if r+2 < row and c+2 < col and is_magic(r,c):
                    res+=1
        return res