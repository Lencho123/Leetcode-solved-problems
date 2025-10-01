class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {}

        def dfs(n):
            if n == 0:
                return 0
            if n in dp:
                return dp[n]
            if n < 0:
                return float("inf")

            temp = float("inf")
            for i in range(len(coins)):
                temp = min(temp, 1+dfs(n-coins[i]))
            
            dp[n] = temp
            return temp

        res = dfs(amount)
        return -1 if res == float("inf") else res