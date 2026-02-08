class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        n = len(nums)
        run_sum = nums[-1]
        count = 0
        for i in range(n-2,-1,-1):
            if nums[i] > run_sum/(n-1-i):
                count+=1
            run_sum+=nums[i]
        return count