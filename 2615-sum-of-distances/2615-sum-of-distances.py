class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        group_ind = defaultdict(list)
        for i,num in enumerate(nums):
            group_ind[num].append(i)
        
        ans = [0 for i in range(len(nums))]
        def help(arr):
            pre_sum = []
            sm = 0
            for ind in arr:
                sm+=ind
                pre_sum.append(sm)

            for i,ind in enumerate(arr):
                ans[ind] = i*ind - (pre_sum[i]-arr[i]) + (pre_sum[-1] - pre_sum[i])-(len(arr) - i-1)*ind 
            
        for key in group_ind:
            help(group_ind[key])
        
        return ans
