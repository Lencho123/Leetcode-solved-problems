class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0]*len(text1) for i in range(len(text2))]

        def in_bound(r,c):
            return 0 <= r < len(text2) and 0 <= c < len(text1)


        for i in range(len(text2)):
            for j in range(len(text1)):
                equal = text1[j] == text2[i]
                left_val = dp[i][j-1] if in_bound(i,j-1) else 0
                top_val = dp[i-1][j] if in_bound(i-1,j) else 0
                top_left = dp[i-1][j-1] if in_bound(i-1,j-1) else 0
                if equal:
                    dp[i][j] = top_left + 1
                else:
                    dp[i][j] = max(left_val, top_val)
        return dp[-1][-1]
