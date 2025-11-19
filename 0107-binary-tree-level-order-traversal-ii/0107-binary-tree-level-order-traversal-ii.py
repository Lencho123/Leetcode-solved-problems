# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        que = deque()
        if root:
            que.append(root)
        res = []

        while que:
            l = len(que)
            row = []
            for i in range(l):
                p = que.popleft()
                row.append(p.val)
                if p.left:
                    que.append(p.left)
                if p.right:
                    que.append(p.right)
            res.append(row)
        return res[::-1]