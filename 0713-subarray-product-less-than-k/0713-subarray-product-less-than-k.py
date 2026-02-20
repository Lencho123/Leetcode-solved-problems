class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left,right,count=0,0,0
        window=nums[left]
        while right<len(nums):
            if window<k:
                count+=right-left+1
                right+=1
                if right<len(nums):
                    window*=nums[right]
            else:
                window/=nums[left]
                left+=1
            if left>right:
                right+=1
                if right<len(nums):
                    window*=nums[right]
        return count
        