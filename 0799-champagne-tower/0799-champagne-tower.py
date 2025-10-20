class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = []
        for i in range(query_row+1):
            row = [0 for j in range(i+1)]
            dp.append(row)

        dp[0][0] = poured
        
        for r in range(1,query_row+1):
            for c in range(len(dp[r])):
                overflow_left = (dp[r-1][c]-1)/2 if 0 <= c < len(dp[r-1]) and dp[r-1][c] > 1 else 0
                overflow_right = (dp[r-1][c-1]-1)/2 if 0 <= c-1 < len(dp[r-1]) and dp[r-1][c-1] > 1 else 0

                dp[r][c] = overflow_left + overflow_right

        return min(1,dp[query_row][query_glass])