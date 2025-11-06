class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        l = 0
        ans = []
        invalid_pair = 0
        for i in range(1,k-1):
            if nums[i] - nums[i-1] != 1:
                invalid_pair+=1

        for r in range(k-1, len(nums)):
            if nums[r] - nums[r-1] != 1:
                invalid_pair+=1

            if invalid_pair == 0:
                ans.append(nums[r])
            else:
                ans.append(-1)
            
            if nums[l+1] - nums[l] != 1:
                invalid_pair-=1 
            l+=1
            
        return ans