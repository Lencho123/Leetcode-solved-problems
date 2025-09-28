class Solution:
    def __init__(self):
        self.map = {}

    def climbStairs(self, n: int) -> int:
        if n == 2 or n == 1:
            return n
        if n-1 not in self.map:
            self.map[n-1] = self.climbStairs(n-1)
        if n-2 not in self.map:
            self.map[n-2] = self.climbStairs(n-2)
        
        return self.map[n-1]+self.map[n-2]