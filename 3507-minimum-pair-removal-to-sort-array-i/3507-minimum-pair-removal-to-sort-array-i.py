class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        res = 0

        def min_pair(arr):
            l,r = 0,1
            sm = float("inf")
            for i in range(1,len(arr)):
                if sm > arr[i]+arr[i-1]:
                    l,r = i-1,i
                    sm = arr[i]+arr[i-1]
            return l,r
        
        def is_sorted(arr):
            for i in range(1,len(arr)):
                if arr[i] < arr[i-1]:
                    return False
            return True

        new_arr = []
        count = 0
        while not is_sorted(nums):
            count+=1
            
            l,r = min_pair(nums)
            i = 0
            left = nums.pop(l)
            right = nums.pop(l)

            nums.insert(l,left+right)
            
        return count