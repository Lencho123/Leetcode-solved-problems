class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = 0
        pre_num = nums[0]
        res = [] 
        nums.sort()
        for i in range(n):
            if pre_num == nums[i]:
                count+=1
            else:
                if count > n/3:
                    res.append(pre_num)
                count = 1
                pre_num = nums[i]
        if count > n/3:
            res.append(pre_num)
        return res