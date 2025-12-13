class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        
        def dfs(ind):
            if ind == len(s):
                return 1
            if s[ind] == "0":
                return 0
            if ind in dp:
                return dp[ind]
            temp = 0
            #take one digit
            temp+=dfs(ind+1)
            #take two digit
            if ind < len(s)-1 and int(s[ind:ind+2]) <= 26:
                temp+=dfs(ind+2)
            dp[ind] = temp
            return dp[ind]
        return dfs(0)
                