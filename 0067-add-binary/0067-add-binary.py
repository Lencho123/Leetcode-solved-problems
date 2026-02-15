class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i,n = 1,max(len(a), len(b))
        carry = 0
        res=""
        
        while i <= n:
            x = int(a[-i]) if i <= len(a) else 0
            y = int(b[-i]) if i <= len(b) else 0

            val = x+y+carry
            if val == 2:
                carry = 1
                val = 0
            elif val == 3:
                carry = 1
                val = 1
            else:
                carry = 0
            i+=1
            
            res=str(val)+res
        
        if carry:
            res="1" + res
        return res