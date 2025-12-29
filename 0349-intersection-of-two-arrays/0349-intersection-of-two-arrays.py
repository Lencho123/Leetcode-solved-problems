class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        
        res = []
        for n in nums1:
            if n in nums2:
                res.append(n)
        return res