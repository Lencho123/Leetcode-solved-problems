# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node,sm):
            if not node.left and not node.right:
                return sm == targetSum
            l,r = False,False
            if node.left:
                l = dfs(node.left,sm+node.left.val)
            if node.right:
                r = dfs(node.right, sm+node.right.val)
            return l or r
        return(dfs(root,root.val))