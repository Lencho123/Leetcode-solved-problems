class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        # if len(nums2) > len(nums1):
        #     nums2,nums1 = nums1,nums2

        dp = {}
        def dfs(ind1,ind2):
            if ind1 == len(nums1) or ind2 == len(nums2):
                return 0
            
            if (ind1,ind2) in dp:
                return dp[(ind1,ind2)]
            
            take = nums1[ind1]*nums2[ind2] + dfs(ind1+1,ind2+1)
            not_take1 = dfs(ind1+1, ind2)
            not_take2 = dfs(ind1, ind2+1)

            dp[(ind1,ind2)] = max(take,not_take1,not_take2)
            return dp[(ind1,ind2)]

        mx1,mn1 = max(nums1), min(nums1)
        mx2,mn2 = max(nums2), min(nums2)

        if mx1 < 0 and mn2 > 0:
            return mx1*mn2
        elif mx2 < 0 and mn1 > 0:
            return mx2*mn1
            
        return dfs(0,0)