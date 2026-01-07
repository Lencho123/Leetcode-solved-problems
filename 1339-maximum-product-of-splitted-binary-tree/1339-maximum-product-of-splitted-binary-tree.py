# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # My strategy is precompute total sum of the tree
        # then current compute at each node and try to maximize the product
        MOD = 10**9 + 7
        dp = {}
        def compute_sum(node):
            if not node:
                return 0

            sm = node.val
            sm+=compute_sum(node.left)
            sm+=compute_sum(node.right)

            dp[id(node)] = sm
            return sm
        
        compute_sum(root)

        res = 0
        total = dp[id(root)]

        def dfs(node):
            nonlocal res
            if not node:
                return

            a = total - dp[id(node)]
            b = dp[id(node)]
            res = max(res, (a*b))

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return res%MOD
