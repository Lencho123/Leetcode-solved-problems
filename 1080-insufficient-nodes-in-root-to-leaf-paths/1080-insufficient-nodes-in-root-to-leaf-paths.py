# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        
        def dfs(sm, node):
            if not node:
                return sm
            
            left_sum = dfs(sm+node.val,node.left)
            right_sum = dfs(sm+node.val,node.right)
            
            temp = 0
            if node.left and node.right:
                temp =  max(left_sum, right_sum)
            elif node.left:
                temp = left_sum
            else:
                temp = right_sum
            
            if left_sum < limit:
                node.left = None
            if right_sum < limit:
                node.right = None
                
            return temp
        
        if dfs(0,root) < limit:
            return None
        return root
            