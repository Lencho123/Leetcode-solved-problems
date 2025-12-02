class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float("inf")

        l,r = 0,len(nums) - 1

        while l <= r:
            m = l + (r-l)//2

            res = min(res, nums[m])
            if nums[l] <= nums[m] <= nums[r]:
                res = min(res,nums[l])
                l+=1
            elif nums[l] <= nums[m]:
                res = min(nums[l], res)
                l = m+1
            elif nums[l] > nums[m]:
                r = m-1
            elif nums[m] <= nums[r]:
                r = m-1
            else:
                res = min(nums[r],res)
                l = m+1
        return res
