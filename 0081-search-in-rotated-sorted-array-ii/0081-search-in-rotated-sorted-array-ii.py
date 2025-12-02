class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l,r = 0,len(nums)-1

        while l <= r:
            m = l + (r-l)//2

            if nums[m] == target:
                return True
            
            # check if duplicate created vague
            if nums[l] <= nums[m] <= nums[r]:
                if nums[l] == target:
                    return True
                l+=1
            # do same as it has no duplicate
            elif nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                if nums[m] <= target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
        return False