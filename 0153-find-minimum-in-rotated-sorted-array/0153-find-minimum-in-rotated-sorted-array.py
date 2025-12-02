class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l,r = 0,len(nums)-1
        res = float("inf")

        while l <= r:
            m = (l+r)//2
            # check sorted part
            if nums[m] < nums[r]: #this is sorted 
                r = m-1
            else:
                l = m+1
            res = min(res, nums[m])
        
        return res