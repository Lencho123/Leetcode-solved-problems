# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        res = 0
        deep = 0
        
        def dfs(node,count):
            nonlocal res,deep
            if not node:
                return count
            
            left = dfs(node.left, count+1)
            right = dfs(node.right, count+1)
            
            if left == right and deep <= left:
                deep = left
                res = node
            
            return max(left,right)
        
        dfs(root,0)
        return res