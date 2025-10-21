# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.is_calculated= False
        self.dp = 0
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}        
        def dfs(node):
            if not node:
                return 0

            if id(node) not in memo:
                take_par = node.val
                if node.left:
                    take_par+=dfs(node.left.left) + dfs(node.left.right)
                if node.right:
                    take_par+=dfs(node.right.left) + dfs(node.right.right)
                
                not_take_par = dfs(node.left) + dfs(node.right)

                memo[id(node)] = max(take_par, not_take_par)

            return memo[id(node)]

        return dfs(root)