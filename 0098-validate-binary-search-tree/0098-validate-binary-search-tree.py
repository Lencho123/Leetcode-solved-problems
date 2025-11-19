# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        lft = float("-inf")
        rgt = float("inf")

        def dfs(left,right,node):
            if not node: return True
            
            if not left < node.val < right:
                return False
            
            l = dfs(left, min(right, node.val),node.left)
            r = dfs(max(left,node.val),right, node.right)
            return l and r
        return dfs(lft,rgt,root)