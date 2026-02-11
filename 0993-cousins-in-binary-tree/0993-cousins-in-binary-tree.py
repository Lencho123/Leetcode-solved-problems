# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        parent = {}
        depth = {}

        def dfs(par,dept,node):
            if not node:
                return
            parent[node.val] = par
            depth[node.val] = dept
            
            dfs(node.val,dept+1,node.right)
            dfs(node.val,dept+1,node.left)
        dfs(-1,0,root)
        if parent[x] != parent[y] and depth[x] == depth[y]:
            return True
        return False
            


        