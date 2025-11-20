# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # do in order traversal and find the two misplassed nodes
        # finally swap them
        pre=left=right=None
        def inorder(node):
            nonlocal right,left,pre
            if not node:
                return
            
            inorder(node.left)
            if not left  and pre and pre.val > node.val:
                left = pre
                right = node
            if left and pre.val > node.val:
                right = node
            pre = node
            inorder(node.right)

        inorder(root)
        right.val,left.val=left.val,right.val
            