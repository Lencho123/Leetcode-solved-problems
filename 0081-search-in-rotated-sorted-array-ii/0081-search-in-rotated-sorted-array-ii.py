class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Let me try devide and conquire

        def dfs(i,j):
            if i == j:
                return nums[i] == target
            if i >= j:
                return False
            
            left = dfs(i,i+(j-i)//2)
            right = dfs((i+(j-i)//2)+1, j)
            return left or right
        return dfs(0, len(nums)-1)