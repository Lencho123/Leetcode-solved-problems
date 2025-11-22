class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # BOTTOM UP SPACE EFFICIENT
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        dp = [False] * (target+1)
        dp[0] = True

        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] = dp[j] or dp[j-num]

        return dp[target]


        # ###  TOP DOWN SOLUTION
        # dp = {}
        # target = sum(nums)/2
        # def canSumUpToHalf(ind,leftSum):
        #     if leftSum == 0:
        #         return True
        #     if leftSum < 0 or ind >= len(nums):
        #         return False
        #     if (ind,leftSum) in dp:
        #         return dp[(ind,leftSum)]
            
        #     temp = False
        #     # Take from ind
        #     temp|= canSumUpToHalf(ind+1,leftSum-nums[ind])
        #     # Not take from ind
        #     temp|= canSumUpToHalf(ind+1, leftSum)
        #     dp[(ind,leftSum)] = temp

        #     return temp

        return canSumUpToHalf(0,target)