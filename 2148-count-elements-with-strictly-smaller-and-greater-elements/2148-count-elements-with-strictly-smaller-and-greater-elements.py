class Solution:
    def countElements(self, nums: List[int]) -> int:
        # SOLUTION-1 O(n^2)
        # ans = 0
        # for i in range(len(nums)):
        #     greater,smaller = False,False
        #     for j in range(len(nums)):
        #         if nums[i] < nums[j]:
        #             greater = True
        #         if nums[i] > nums[j]:
        #             smaller = True
        #     if greater and smaller:
        #         ans+=1
        # return ans


        #SOLUTION-2 O(n)
        ans = 0
        min_val = min(nums)
        max_val = max(nums)

        for i in range(len(nums)):
            if min_val < nums[i] < max_val:
                ans+=1
        return ans
