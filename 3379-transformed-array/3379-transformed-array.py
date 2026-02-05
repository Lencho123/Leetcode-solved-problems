class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        visited = set()
        result = nums[:]
        
        for i in range(len(nums)):
            ind = 0
            ind = (i+nums[i])%len(nums)
    
            result[i] = nums[ind]

        return result