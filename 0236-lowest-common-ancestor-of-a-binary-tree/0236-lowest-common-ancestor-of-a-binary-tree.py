# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        flag = False
        res = None
        
        def dfs(node):
            nonlocal res, flag
            if not node:
                return False,False
            
            foundp = True if node.val == p.val else False
            foundq = True if node.val == q.val else False
            
            leftp,leftq = dfs(node.left)
            rightp,rightq = dfs(node.right)
            
            foundp|=leftp|rightp
            foundq|=leftq|rightq
            
            if not flag and foundp and foundq:
                flag = True
                res = node
            
            return foundp,foundq
        
        dfs(root)
        return res