class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        num1XOR = 0
        num2XOR = 0
        if len(nums2)%2:
            for num in nums1:
                num1XOR^=num
        if len(nums1)%2:
            for num in nums2:
                num2XOR^= num

        return num1XOR^num2XOR