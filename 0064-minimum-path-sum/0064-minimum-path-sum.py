class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}
        m,n = len(grid),len(grid[0])

        def dfs(i,j):
            if i == m-1 and j == n-1:
                return grid[i][j]
            
            r,c = i+1,j+1
            if (i,j) in dp:
                return dp[(i,j)]
            if i == m-1:
                dp[(i,j)] = grid[i][j] + dfs(i,j+1)
            elif j == n-1:
                dp[(i,j)] = grid[i][j] + dfs(i+1,j)
            else:
                dp[(i,j)] = grid[i][j] + min(dfs(i,j+1),dfs(i+1,j))

            return dp[(i,j)]

        return dfs(0,0)

        