# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
            
        stack = []
        res = []
        def dfs(node,sm):
            stack.append(node.val)
            if not node.left and not node.right:
                if sm == targetSum:
                    res.append(stack.copy())
                stack.pop()
                return
            
            if node.left:
                dfs(node.left, sm+node.left.val)
            if node.right:
                dfs(node.right,sm+node.right.val)

            # backtrack
            stack.pop()

        dfs(root,root.val)
        return res