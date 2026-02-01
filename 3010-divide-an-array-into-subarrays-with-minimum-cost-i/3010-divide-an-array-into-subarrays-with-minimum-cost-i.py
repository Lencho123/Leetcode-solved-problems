class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first = nums[0]
        sorted_nums = sorted(nums[1:])
        
        return first + sorted_nums[0] + sorted_nums[1]
