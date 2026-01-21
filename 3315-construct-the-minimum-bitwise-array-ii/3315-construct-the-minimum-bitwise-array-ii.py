class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        def find_min_bw(num):
            if num == 2: return -1
            pos = 0
            res = 0

            while True:
                if not (num & 1):
                    res-=2**(pos-1)
                    break
                res+=2**pos
                pos+=1
                num>>=1
            
            while num:
                res+=(num&1)*(2**pos)
                pos+=1
                num>>=1
            
            return res
        
        for n in nums:
            ans.append(find_min_bw(n))
        return ans