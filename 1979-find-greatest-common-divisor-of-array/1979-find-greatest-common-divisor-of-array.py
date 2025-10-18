class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a,b):
            mx = max(a,b)
            mn = min(a,b)
            a=mx
            b = mn
            if a%b == 0:
                return b
            return gcd(b,a%b)
        
        # res = gcd(nums[0], nums[1])
        # for i in range(2,len(nums)):
        #     res = gcd(res,nums[i])
        
        return gcd(max(nums), min(nums))