class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return 0
        hash = set([1])

        for i in range(2, n):
            j = i
            if i in hash:
                continue
            while i*j < n:
                hash.add(i*j)
                j+=1
        return n-1-len(hash)