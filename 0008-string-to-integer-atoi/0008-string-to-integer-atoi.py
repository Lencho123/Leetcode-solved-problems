class Solution:
    def myAtoi(self, s: str) -> int:
        def strip(st):
            for i,d in enumerate(st):
                if d != " ":
                    return st[i:]
            return ""
        
        ans = ""
        s = strip(s)
        
        
        digits = "1234567890"
        for i,d in enumerate(s):
            if i == 0 and d in "-+":
                ans+=d
            elif d not in digits:
                break
            else:
                ans+=d
                
        ans = int(ans) if (ans != "+" and ans != "-" and ans != "") else 0

        if ans > 2**31 - 1: return 2**31 - 1
        if ans < -2**31: return -2**31
        return ans
             