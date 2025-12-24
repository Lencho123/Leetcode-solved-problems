class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            l = i+1
            r = len(nums)-1
            
            while l < r:
                    
                sm = nums[i]+nums[l]+nums[r]
                
                if sm == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    
                    while l < r and nums[l-1] == nums[l]:
                        l+=1
                    while l < r<len(nums) and nums[r] == nums[r+1]:
                        r-=1
                        
                elif sm > 0:
                    r-=1
                else:
                    l+=1
                    
                
        return res