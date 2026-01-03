class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        def is_valid(prev1,prev2,prev3,c1,c2,c3):
            if prev1 == c1 or prev2 == c2 or prev3 == c3:
                return False
            if c1 == c2 or c2 == c3:
                return False
            return True
        
        dp = {}

        def dfs(col1,col2,col3, step):
            if step == n:
                return 1
            if (col1,col2,col3, step) in dp:
                return dp[(col1,col2,col3, step)]

            ans = 0
            for c1 in range(1,4):
                for c2 in range(1,4):
                    for c3 in range(1,4):
                        if is_valid(col1,col2,col3,c1,c2,c3):
                            ans+=dfs(c1,c2,c3, step+1)%MOD
            dp[(col1,col2,col3, step)] = ans%MOD
            return dp[(col1,col2,col3, step)]

        return dfs(0,0,0,0)