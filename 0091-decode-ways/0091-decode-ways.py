class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        dp = defaultdict(int)
        def dfs(i):
            if i == len(s):
                return 1 
            
            if s[i] == "0":
                return 0

            if (i+1,i+1) not in dp:
                dp[(i+1,i+1)] = dfs(i+1)
            if i < len(s) - 1 and "10" <= s[i:i+2] <= "26" and (i+1,i+2) not in dp:
                dp[(i+1,i+2)] = dfs(i+2)
            return dp[(i+1,i+1)] + dp[(i+1,i+2)]
        
        return dfs(0)