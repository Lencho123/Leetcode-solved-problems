class Solution:
    def __init__(self):
        self.hash = {}
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        if n == 2:
            return 1

        if n-3 not in self.hash:
            self.hash[n-3] = self.tribonacci(n-3)
        if n-2 not in self.hash:
            self.hash[n-2] = self.tribonacci(n-2)
        if n-1 not in self.hash:
            self.hash[n-1] = self.tribonacci(n-1)
            
        return  self.hash[n-1] +  self.hash[n-2] +  self.hash[n-3]