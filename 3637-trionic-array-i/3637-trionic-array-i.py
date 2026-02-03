class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        
        p,q = 0,n-1

        for i in range(n):
            if i == n-1:
                return False 

            if nums[i] >= nums[i+1]:
                p = i
                break

        for i in range(n-1,-1,-1):
            if i == 0:
                return False
            
            if nums[i-1] >= nums[i]:
                q = i
                break
        
        for i in range(p,q):
            if nums[i+1] > nums[i]:
                return False
        
        if p == 0 or q == n-1:
            return False
            
        return True