# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #set right sum and return whole sum
        #right,left,root
        com_sum = 0
        
        def dfs(node):
            nonlocal com_sum
            if not node:
                return
            
            dfs(node.right)
            
            com_sum+=node.val
            node.val=com_sum
            
            dfs(node.left)
        
        dfs(root)
        
        return root