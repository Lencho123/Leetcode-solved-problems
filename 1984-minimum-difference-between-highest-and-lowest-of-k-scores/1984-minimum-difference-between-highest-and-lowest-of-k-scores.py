class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        mindiff=float("inf")
        left=0
        for right in range(k-1,len(nums)):
            mindiff=min(mindiff, nums[right]-nums[left])
            left+=1
        return mindiff

        