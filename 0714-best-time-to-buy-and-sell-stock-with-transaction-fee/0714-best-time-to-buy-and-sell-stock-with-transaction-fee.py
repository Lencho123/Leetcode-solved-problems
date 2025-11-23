class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        dp = {}
        # we have state (buy,index)

        def trade(ind,buy):
            if ind == len(prices):
                return 0
            
            if (ind,buy) in dp:
                return dp[(ind,buy)]
            
            temp = float("-inf")
            if buy:
                temp = max(temp, -prices[ind]+trade(ind+1, not buy))
            else:
                temp = max(temp, prices[ind]-fee + trade(ind+1, not buy))
            # Neither buy nor sell
            temp = max(temp, trade(ind+1, buy))
            dp[(ind,buy)] = temp
            return dp[(ind,buy)]
        
        return trade(0,True)