# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def to_decimal(binary):
            l = len(binary)
            res = 0
            for i in range(l):
                bit = 1 if binary[-(i+1)] == "1" else 0
                res+= bit*(2**i)
            return res

        def dfs(node, val):
            nonlocal ans
            if not node.left and not node.right:
                ans+=to_decimal(val)
                return
            
            if node.left:
                dfs(node.left, val+str(node.left.val))
            if node.right:
                dfs(node.right, val+str(node.right.val))
        dfs(root,str(root.val))
        return ans