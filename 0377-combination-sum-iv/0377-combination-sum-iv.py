class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(sm,ind):
            if sm == target:
                return 1
            if sm > target:
                return 0
            
            temp = 0
            if (sm,nums[ind]) not in dp:
                for i in range(len(nums)):
                    temp+=dfs(sm+nums[i], i)
                dp[(sm,nums[ind])] = temp
                
            return dp[(sm,nums[ind])]

        return dfs(0,0)