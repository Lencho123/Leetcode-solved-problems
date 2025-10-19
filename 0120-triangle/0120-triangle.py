class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = {}

        def dfs(sm, row, col):
            if row == len(triangle)-1:
                return triangle[row][col]
            
            if (row+1,col) not in dp:  
                dp[(row+1,col)] = dfs(sm+triangle[row+1][col], row+1,col)
            if (row+1,col+1) not in dp:
                dp[(row+1,col+1)] = dfs(sm+triangle[row+1][col+1], row+1,col+1)

            return min(dp[(row+1,col)],dp[(row+1,col+1)]) + triangle[row][col]
        return dfs(0,0,0)