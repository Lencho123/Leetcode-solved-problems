# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_indices = {}
        for i,val in enumerate(inorder):
            in_indices[val] = i
        ptr = 0

        def construct(start,end):
            nonlocal ptr
            if start > end:
                return
            
            pre = preorder[ptr]
            
            root = TreeNode(pre)
            mid_ind = in_indices[pre]

            ptr+=1

            root.left = construct(start, mid_ind-1)
            root.right = construct(mid_ind+1,end)

            return root
        
        return construct(0,len(inorder)-1)