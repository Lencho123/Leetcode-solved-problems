class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(num):
            if num == 2: return True
            if num == 1: return False
            for i in range(2,num):
                if num%i == 0:
                    return False
            return True

        res = 0
        for i in range(left,right+1):
            num = i.bit_count()
            res+=is_prime(num)
        return res