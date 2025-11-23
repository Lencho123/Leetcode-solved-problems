class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
         
        dp = {}

        def dfs(ind):

            if ind in dp:
                return dp[ind]
            
            temp = 1
            for i in range(ind,len(nums)):
                if nums[ind] < nums[i]:
                    temp = max(temp, 1+dfs(i))
            dp[ind] = temp
            return dp[ind]
            
        return max(dfs(i) for i in range(len(nums)))