class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)/2
        sums = set()
        
        for i in range(len(nums)):
            cur_sums = set([])|sums
            for s in cur_sums:
                if target >= s+nums[i]:
                    sums.add(s+nums[i])
            sums.add(nums[i])

        if target in sums:
            return True

        return False