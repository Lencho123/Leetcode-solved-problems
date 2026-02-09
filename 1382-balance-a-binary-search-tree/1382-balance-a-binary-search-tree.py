# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorderTraverse(root):
            if not root:
                return
            
            inorderTraverse(root.left)
            sorted_list.append(root.val)
            inorderTraverse(root.right)

        sorted_list = []
        inorderTraverse(root)

        def balanced(new_root, l):
            m = len(l)//2

            left = l[:m]
            right = l[m+1:]
            lm = len(left)//2
            rm = len(right)//2

            if len(l) == 0:
                return
            if len(left)>0:
                new_root.left = TreeNode(left[lm])
                balanced(new_root.left, left)

            if len(right)>0:
                new_root.right = TreeNode(right[rm])
                balanced(new_root.right, right)
        
        new_root = TreeNode(sorted_list[len(sorted_list)//2])
        balanced(new_root,sorted_list)

        return new_root