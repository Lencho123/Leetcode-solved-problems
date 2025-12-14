class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        
        while l < r:
            m = l + (r-l)//2
            left = nums[m-1] if m>0 else -1
            right = nums[m+1] if m < len(nums)-1 else -1

            if left != nums[m] and right != nums[m]:
                return nums[m]
            elif left == nums[m]:
                if len(nums[l:m+1])%2:
                    r = m
                else:
                    l = m+1
            else:
                if len(nums[m:])%2:
                    l = m
                else:
                    r = m-1
        return nums[r]
                    