class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        area = 0

        row, col = len(matrix),len(matrix[0])
        dp = [[[0,0] for i in range(col)] for j in range(row)] #(rowcount,colcount)

        for r in range(row):
            for c in range(col):
                top_count = dp[r-1][c][1] if r-1 >= 0 else 0
                left_count = dp[r][c-1][0] if c-1 >= 0 else 0

                if matrix[r][c] == "1":
                    dp[r][c] = [left_count+1, top_count+1]

        #Calculate max area
        for r in range(row):
            for c in range(col):
                h = dp[r][c][1]
                for i in range(c, col):
                    if matrix[r][i] == "0":
                        break

                    b = i-c+1
                    h = min(h, dp[r][i][1])  
                    area = max(area, b*h)      

        return area