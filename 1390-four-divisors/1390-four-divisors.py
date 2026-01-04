class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        def factorize(num):
            factors = set([num])
            d = 2
            while num > 1:
                while num%d == 0:
                    num/=d
                    factors.add(num)
                    factors.add(d)

                if len(factors) > 4:
                    return 0
                d+=1
            factors = list(factors)
            if len(factors) == 4:
                return sum(factors)
            return 0

        res = 0
        for num in nums:
            res+=factorize(num)
        return int(res)