class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        stack = []
        def computeXOR(arr):
            res = 0
            for i in arr:
                res^=nums[i-1]
            return res
        ans,stack = 0,[]
        visited = set()

        def backtrack(ind):
            nonlocal ans,stack

            if ind == len(nums):
                return
            
            for i in range(ind,len(nums)):
                stack.append(i)
                backtrack(i+1)
                ans += computeXOR(stack)
                # print(stack)
                stack.pop()

        backtrack(0)
        return ans