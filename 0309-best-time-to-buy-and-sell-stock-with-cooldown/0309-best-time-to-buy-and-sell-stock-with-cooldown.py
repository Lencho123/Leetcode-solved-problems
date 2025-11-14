class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i,buying) in dp:
                return dp[(i,buying)]
            
            cool = dfs(i+1,buying)
            sell,buy = 0,0

            if buying:
                buy+=-prices[i] + dfs(i+1, not buying)
            else:
                sell+=prices[i] + dfs(i+2, not buying)
            
            dp[(i,buying)] = max(cool,buy,sell)
            return dp[(i,buying)]
        
        res = 0
        for i in range(len(prices)):
           res = max(res, dfs(i,True))
        return res