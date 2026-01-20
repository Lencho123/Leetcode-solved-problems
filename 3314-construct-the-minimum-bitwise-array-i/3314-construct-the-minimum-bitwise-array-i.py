class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]: 
        ans = []

        def find_min_bw(num):
            for i in range(num):
                if num == i|(i+1):
                    return i
            return -1
        
        for n in nums:
            ans.append(find_min_bw(n))
        return ans