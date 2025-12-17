class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pre_sum = [0]*1001
        
        for pas,fro,to in trips:
            pre_sum[fro]+=pas
            pre_sum[to]-=pas
        
        for i in range(1001):
            if i > 0:
                pre_sum[i]+=pre_sum[i-1]
            if pre_sum[i] > capacity: return False
        
        return True