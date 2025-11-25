class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # # # ===TOP DOWN SOLUTION with two state (cur_index,prev_index) More Intuitive [TAKE, NOT_TAKE]===
        # dp = {}
        # def dfs(cur_ind,prev_ind):
        #     if cur_ind == len(nums):
        #         return 0
            
        #     if (cur_ind,prev_ind) in dp:
        #         return dp[(cur_ind,prev_ind)]
            
        #     take, not_take = 0,0
        #     if prev_ind == -1 or nums[cur_ind] > nums[prev_ind]:
        #         # take
        #         take = 1+dfs(cur_ind+1,cur_ind)
        #     # not take
        #     not_take = dfs(cur_ind+1,prev_ind)
        #     dp[(cur_ind,prev_ind)] = max(take,not_take)
        #     return dp[(cur_ind,prev_ind)]

        # return dfs(0,-1)
        
        # BOTTOM UP APPROACH
        n = len(nums)
        DP = [1]*n
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if nums[i] < nums[j]:
                    DP[i] = max(DP[i], 1+DP[j])
        return max(DP)


        # # ===TOP DOWN SOLUTION (less intuitive to me)===
        # dp = {}
        # def dfs(ind):

        #     if ind in dp:
        #         return dp[ind]
            
        #     temp = 1
        #     for i in range(ind,len(nums)):
        #         if nums[ind] < nums[i]:
        #             temp = max(temp, 1+dfs(i))
        #     dp[ind] = temp
        #     return dp[ind]
            
        # return max(dfs(i) for i in range(len(nums)))