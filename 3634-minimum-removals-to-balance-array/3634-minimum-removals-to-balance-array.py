class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        res = float("inf")

        l,r = 0,0
        while r < n:
            if nums[l]*k >= nums[r]:
                r+=1
                res = min(l+n-r,res)
            else:
                l+=1
        return res
            