class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        row,col = len(grid), len(grid[0])
        def in_bound(r,c):
            return 0<=r<row and 0<=c<col
        
        def dfs(r,c):
            if r == 0 or r == row-1 or c == 0 or c == col-1:
                return False
            
            grid[r][c] = 1
            
            temp = True
            for dr,dc in directions:
                nr = dr+r
                nc = dc+c
                if in_bound(nr,nc) and grid[nr][nc] == 0:
                    temp&=dfs(nr,nc)
                
            return temp
        
        res = 0
            
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    res+=dfs(i,j)
        return res