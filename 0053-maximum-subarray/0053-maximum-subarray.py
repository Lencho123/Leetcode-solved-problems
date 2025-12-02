class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)

        run_sum = 0
        for n in nums:
            run_sum+=n
            run_sum = max(n, run_sum)

            res = max(res,run_sum)
        return res