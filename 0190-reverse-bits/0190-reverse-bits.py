class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        x = 31
        for i in range(32):
            if n == n|1:
                res|=2**x
            n>>=1
            x-=1
        return res