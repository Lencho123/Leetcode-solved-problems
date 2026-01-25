class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return "0"
        res = []
        negative = False
        
        if num < 0:
            negative = True
        num = abs(num)
        
        while num:
            res.append(str(num%7))
            num//=7
        
        res = "".join(res[::-1])
        
        return res if not negative else "-"+res