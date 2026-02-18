class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        alt = n&1
        n>>=1

        while n:
            if n&1 == alt:
                return False
            alt = n&1
            n>>=1
        return True