class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float("-inf")

        presum = [0]

        for i,num in enumerate(nums):
            presum.append(presum[-1]+num)
    
        i = 0
        while i < n-1:
            left = i
            left_min = presum[i]
            # first increase
            if i >= n-1 or not nums[i] < nums[i+1]:
                i+=1
                continue
            while i < n-1 and nums[i] < nums[i+1]:
                left_min = min(left_min, presum[i])
                i+=1
            
            peak = i
            # second decreasing
            if i >= n-1 or not nums[i] > nums[i+1]: 
                i+=1
                continue
            while i < n-1 and nums[i] > nums[i+1]:
                i+=1
            
            valley = i
            #thrid increasing
            if i >= n-1 or not nums[i] < nums[i+1]:
                i+=1
                continue
            
            right_max = presum[i+2]
            while i < n-1 and nums[i] < nums[i+1]:
                right_max = max(right_max, presum[i+2])
                i+=1
            
            ans = max(ans, right_max-left_min)
            i=valley
        
        return ans

