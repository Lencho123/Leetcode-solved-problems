# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
    
        def bfs(node):
            que = deque()
            leaf = False
            que.append(node)
            while que:
                p = que.popleft()
                if not p.left and p.right:
                    return False
                
                if leaf:
                    if p.left or p.right:
                        return False
                    
                if p.left:
                    que.append(p.left)
                if p.right:
                    que.append(p.right)

                if not p.left or not p.right:
                    leaf = True

            return True

        return bfs(root)