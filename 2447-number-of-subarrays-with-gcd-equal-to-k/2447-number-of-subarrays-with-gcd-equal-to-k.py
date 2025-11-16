class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            cur_gcd = nums[i]
            for j in range(i, len(nums)):
                cur_gcd = math.gcd(cur_gcd, nums[j])
                if cur_gcd == k:
                    count+=1
        return count