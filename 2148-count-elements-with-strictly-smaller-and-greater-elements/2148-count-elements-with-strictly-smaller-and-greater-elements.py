class Solution:
    def countElements(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums)):
            greater,smaller = False,False
            for j in range(len(nums)):
                if nums[i] < nums[j]:
                    greater = True
                if nums[i] > nums[j]:
                    smaller = True
            if greater and smaller:
                ans+=1
                
        return ans
