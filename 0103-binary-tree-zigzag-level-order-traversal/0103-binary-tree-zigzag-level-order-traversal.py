# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(root):
            nonlocal res,to_left
            if not root:
                return
            
            q = deque([root])
            while q:
                l = len(q)
                row = []
                for i in range(l):
                    node = q.popleft()
                    row.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                if to_left:
                    row.reverse()
                    to_left = False
                else:
                    to_left=True
                res.append(row)
            
        res = []
        to_left = False
        bfs(root)
        return res