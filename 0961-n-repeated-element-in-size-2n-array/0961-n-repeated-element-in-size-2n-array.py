class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        l = len(nums)
        count = Counter(nums)
        
        for c in count:
            if count[c] == l/2:
                return c
            