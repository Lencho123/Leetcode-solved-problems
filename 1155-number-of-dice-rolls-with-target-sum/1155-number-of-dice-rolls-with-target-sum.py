class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        dp = {}
        
        def dfs(cur_val,throw):
            if cur_val == 0 and throw == 0:
                return 1
            if cur_val < 0 or throw < 0:
                return 0
            
            if (cur_val,throw) in dp:
                return dp[(cur_val,throw)]
            
            temp = 0
            for i in range(1,k+1):
                temp+=dfs(cur_val-i, throw-1)
            dp[(cur_val,throw)] = temp%MOD
            return dp[(cur_val,throw)]
        
        return dfs(target,n)
        