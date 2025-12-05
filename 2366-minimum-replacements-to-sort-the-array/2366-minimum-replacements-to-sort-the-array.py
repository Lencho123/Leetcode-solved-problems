class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        min_val=nums[-1]
        res = 0
        for i in range(len(nums)-1, -1, -1):
            av = ceil(nums[i]/min_val)
            res+=max(av-1, 0)
            min_val = min(min_val, nums[i]//av)

        return res