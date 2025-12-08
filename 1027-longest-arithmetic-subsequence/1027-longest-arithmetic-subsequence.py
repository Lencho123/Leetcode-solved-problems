class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        def find_longest(diff):
            dp = defaultdict(int)
            
            for i in range(len(nums)):
                prev = nums[i] - diff
                
                if prev not in dp:
                    dp[nums[i]] = 1
                else:
                    dp[nums[i]] = dp[prev]+1
                    
            return max(dp.values())
        
        rang = max(nums)-min(nums)+2
        res = 0
        
        for i in range(rang):
            res = max(res,find_longest(i))
            res = max(res,find_longest(-i))
        return res