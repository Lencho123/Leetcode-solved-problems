class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0 for i in range(n)]
        dp[n-1] = questions[n-1][0]

        for i in range(n-2, -1, -1):
            dp[i] = max(dp[i+1], questions[i][0] + (dp[i+questions[i][1]+1] if i+questions[i][1]+1 < n else 0))
        
        return dp[0]
