# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return None

        right = root.right
        left = root.left

        self.flatten(left)
        self.flatten(right)
        
        tail = root
        root.right = left
        while tail.right:
            tail = tail.right
        
        tail.right = right
        root.left = None
        
        """
        Do not return anything, modify root in-place instead.
        """
        