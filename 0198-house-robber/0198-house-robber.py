class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        hash ={}
        hash[0] = nums[0]
        hash[1] = max(nums[0],nums[1])
        
        def dp(n):
            if n == 0 or n == 1:
                return nums[n]
            if n-1 not in hash:
                hash[n-1] = dp(n-1)
            if n-2 not in hash:
                hash[n-2] = dp(n-2)
            hash[n] = max(hash[n-1], nums[n]+hash[n-2])
            return hash[n]
        
        return dp(len(nums)-1)