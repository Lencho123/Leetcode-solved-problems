class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(t, index):
            nonlocal dp
            if index < 0:
                return 1 if t == target else 0
            
            take = 0
            not_take = 0

            if (t,index) in dp:
                return dp[(t,index)]
            
            take = dfs(t+nums[index], index-1)
        
            not_take = dfs(t-nums[index], index-1)
            dp[(t,index)] = take + not_take
            
            return take+not_take
        
        return dfs(0,len(nums)-1)