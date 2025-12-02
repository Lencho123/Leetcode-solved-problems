class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r,n = 0,len(nums)-1,len(nums)

        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target:
                return m
            # identify sorted half
            r_sorted = False
            if nums[m] <= nums[r]:
                r_sorted = True
            
            if r_sorted:
                # check if element is in right porsion
                if nums[m] <= target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
            else:
                # check if nums is in left porsion
                if nums[l] <= target <= nums[m]:
                    r = m-1
                else:
                    l = m+1
                    
        return -1
