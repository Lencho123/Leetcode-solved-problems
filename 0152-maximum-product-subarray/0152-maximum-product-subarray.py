class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        
        product = 1
        for num in nums:
            if num == 0:
                product = 1
            else:
                product *= num
                result = max(result, product)
        
        product = 1
        for num in nums[::-1]:
            if num == 0:
                product = 1
            else:
                product *= num
                result = max(result, product)
        
        return result