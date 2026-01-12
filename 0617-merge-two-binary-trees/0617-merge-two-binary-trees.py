# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node1,node2):
            if not node1 and not node2:
                return None
            
            new_node = None
            
            if node1 and node2:
                new_node = TreeNode(node1.val+node2.val)
            elif node1:
                new_node = TreeNode(node1.val)
            elif node2:
                new_node = TreeNode(node2.val)
                
            left1 = node1.left if node1 else None
            right1 = node1.right if node1 else None
            
            left2 = node2.left if node2 else None
            right2 = node2.right if node2 else None
            
            
            new_node.left = dfs(left1,left2)
            new_node.right = dfs(right1,right2)
            
            return new_node
        
        return dfs(root1,root2)