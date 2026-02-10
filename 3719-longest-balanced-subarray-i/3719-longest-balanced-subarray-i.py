class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        
        # hash=defaultdict(int)
        longest = 0

        for i in range(len(nums)):
            hash=set()
            o_count = 0
            e_count = 0
            for j in range(i,len(nums)):
                if nums[j] not in hash:
                    o_count+=nums[j]%2
                    e_count+=nums[j]%2 == 0
                if e_count == o_count:
                    longest = max(longest,j-i+1)
                hash.add(nums[j])
        return longest
                