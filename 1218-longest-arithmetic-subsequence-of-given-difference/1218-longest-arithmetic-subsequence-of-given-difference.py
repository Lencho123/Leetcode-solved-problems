class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        res = 0

        for i in range(len(arr)):
            x = arr[i] - difference 
            if x in dp:
                dp[arr[i]] = (i,dp[x][1]+1)
            else:
                dp[arr[i]] = (i,0)
            res = max(res, dp[arr[i]][1])

        return res+1