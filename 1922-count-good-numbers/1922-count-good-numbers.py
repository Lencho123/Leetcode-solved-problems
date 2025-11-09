class Solution:
    def countGoodNumbers(self, n: int) -> int:
        odd=even = n//2
        if n%2:
            even+=1
        return (pow(5,even,1000000007)*pow(4,odd,1000000007))%1000000007