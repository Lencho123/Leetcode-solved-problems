class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        group_ind = defaultdict(list)
        for i,num in enumerate(arr):
            group_ind[num].append(i)
        
        ans = [0 for i in range(len(arr))]
        def help(arr_same_inds):
            pre_sum = []
            sm = 0
            for ind in arr_same_inds:
                sm+=ind
                pre_sum.append(sm)

            for i,ind in enumerate(arr_same_inds):
                ans[ind] = i*ind - (pre_sum[i]-arr_same_inds[i]) + (pre_sum[-1] - pre_sum[i])-(len(arr_same_inds) - i-1)*ind 
            
        for key in group_ind:
            help(group_ind[key])
        
        return ans
