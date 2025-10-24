class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        l = []
        while x:
            l.append(x%10)
            x//=10
        
        return l == l[::-1]