# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        level = 0
        max_sum = root.val
        res = 1

        que = deque([root])
        while que:
            l = len(que)
            cur_sum = 0
            level+=1

            for i in range(l):
                p = que.popleft()
                cur_sum+=p.val

                if p.left: que.append(p.left)
                if p.right: que.append(p.right)
            
            if max_sum < cur_sum:
                max_sum = cur_sum
                res = level
        return res