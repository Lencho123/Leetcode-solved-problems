class Solution:
    def numSquares(self, n: int) -> int:
        dp = {}
        def dfs(sm):
            # print(sm)
            if sm == n:
                return 0
            if sm > n:
                return float("inf")
            if sm in dp:
                return dp[sm]
            temp = float("inf")
            for i in range(1,int(n**0.5)+2):
                temp = min(temp, dfs(sm+i**2))
            dp[sm] = temp+1
            return dp[sm]


        return dfs(0)