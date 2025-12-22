class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = {}
        mod = 10**9 + 7
        def dfs(n,prev,consec):
            if n == 0:
                return 1
            if (n,prev,consec) in dp:
                return dp[(n,prev,consec)]
            temp = 0
            for i in range(6):
                if prev == i:
                    if consec < rollMax[i]:
                        temp+=dfs(n-1,prev,consec+1)
                else:
                    temp+=dfs(n-1,i,1)
                
            dp[(n,prev,consec)] = temp%mod
            return dp[(n,prev,consec)]
        
        return dfs(n,-1,1)