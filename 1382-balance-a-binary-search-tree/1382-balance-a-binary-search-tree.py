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

        def build_balanced_tree(l,r):
            if l > r:
                return None
            
            m = (l+r)//2
            new_root = TreeNode(sorted_list[m])
            new_root.left = build_balanced_tree(l,m-1)
            new_root.right = build_balanced_tree(m+1,r)

            return new_root


        return build_balanced_tree(0,len(sorted_list)-1)