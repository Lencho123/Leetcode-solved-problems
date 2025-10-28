# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def countLevel(node):
            res = []
            que = deque()
            if node:
                que.append(node)

            while que:
                l = len(que)

                for i in range(l):
                    p = que.popleft()
                    if p.left:
                        que.append(p.left)
                    if p.right:
                        que.append(p.right)
                    if i == l-1:
                        res.append(p.val)

            return res
        return countLevel(root)