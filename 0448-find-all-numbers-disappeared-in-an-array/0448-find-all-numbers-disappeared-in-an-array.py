class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        def put_on_their_index():
            for i, n in enumerate(nums):
                nums[i],nums[n-1] = nums[n-1],nums[i]
                
        #call the function twice to insure all possible sit on their corrisponding index
        put_on_their_index()
        put_on_their_index()
        put_on_their_index()
        put_on_their_index()
        
        res = []
        for i, n in enumerate(nums):
            if i+1 != n:
                res.append(i+1)
        return res