# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        in_inds = {}
        for i,val in enumerate(inorder):
            in_inds[val] = i

        ptr = len(postorder) - 1
        def construct(start,end):
            nonlocal ptr
            if start > end:
                return None
            
            post = postorder[ptr]
            root = TreeNode(post)

            ptr-=1
            mid_in = in_inds[post]

            root.right = construct(mid_in+1, end)
            root.left = construct(start, mid_in-1)

            return root
    
        return construct(0,len(postorder) - 1)