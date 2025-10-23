class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dp = [[float("inf")]*26 for i in range(26)]
        
        for i in range(len(original)):
            r,c=ord(original[i])-ord("a"), ord(changed[i])-ord("a")
            dp[r][c] = min(dp[r][c],cost[i])
        
        for via in range(26):
            for i in range(26):
                for j in range(26):
                    dp[i][j] = min(dp[i][j], dp[i][via] + dp[via][j])
                    if i == j:
                        dp[i][j] = 0
        
        res = 0
        for i in range(len(source)):
            r,c = ord(source[i])-ord("a"), ord(target[i])-ord("a")
            res+=dp[r][c]

        return res if res<float("inf") else -1
