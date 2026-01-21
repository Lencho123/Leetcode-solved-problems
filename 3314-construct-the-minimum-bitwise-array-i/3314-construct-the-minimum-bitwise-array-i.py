class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]: 
        ans = []

        def find_min_bw(num):
            if num == 2: return -1
            flag = True
            pos = 0
            res = 0
            while flag:
                if not num & 1:
                    flag = False
                    res-=2**(pos-1)
                else:
                    res+=2**pos
                    num>>=1
                    pos+=1

            while num:
                res+=(num&1)*2**pos
                num>>=1
                pos+=1
            return res
            
        for n in nums:
            ans.append(find_min_bw(n))
        return ans