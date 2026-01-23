class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry = 0
        
        for i in range(len(num)-1,-1,-1):
            digit = k%10
            
            sm = carry + digit + num[i]
            if sm >= 10:
                carry = 1
            else:
                carry = 0
            
            sm%=10
            
            num[i] = sm
            k//=10
        
        while k:
            digit = k%10
            sm = carry + digit
            if sm >= 10:
                carry = 1
            else:
                carry = 0
            sm%=10
            num.insert(0,sm)
            k//=10
            
        if carry:
            num.insert(0,1)
        
        return num
            