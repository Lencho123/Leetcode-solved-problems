class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1]+=1
            return digits
        
        index = -1
        for i in range(len(digits)-1,-1,-1):
            if digits[i]!=9:
                break
            index=i
        
        digits[index] = 1
        for i in range(index+1, len(digits)):
            digits[i] = 0
        digits.append(0)

        return digits