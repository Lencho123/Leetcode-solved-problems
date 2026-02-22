class Solution:
    def binaryGap(self, n: int) -> int:
        res = 0
        # remove first cosicutive zeros from left
        while not n&1:
            n>>=1

        count = 0
        res = 0

        while n:
            # remove consicutive ones
            while n&1 and (n>>1)&1:
                res = max(res,1)
                n>>=1

            n>>=1
            count+=1
            if n&1:
                res = max(res,count)
                count = 0
        return res