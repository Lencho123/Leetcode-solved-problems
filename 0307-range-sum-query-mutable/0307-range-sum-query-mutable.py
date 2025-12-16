class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pre_sum = [nums[0]]
        for i in range(1,len(self.nums)):
            self.pre_sum.append(self.pre_sum[-1]+self.nums[i])

    def update(self, index: int, val: int) -> None:
        dif = val-self.nums[index]
        self.nums[index] = val
        for i in range(index, len(self.pre_sum)):
            self.pre_sum[i]+=dif

    def sumRange(self, left: int, right: int) -> int:
        left_sum = self.pre_sum[left-1] if left > 0 else 0
        right_sum = self.pre_sum[right]
        return right_sum - left_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)