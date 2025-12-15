# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        res = 1

        que = deque([[root, 0]])

        while que:
            l = len(que)
            nd,start_ind = que[0]
            width = 1
            for _ in range(l):
                node,cur_ind = que.popleft()
                width = cur_ind - start_ind + 1

                if node.left:
                    que.append([node.left,cur_ind*2 + 1])
                if node.right:
                    que.append([node.right,cur_ind*2 + 2])
            res = max(res,width)
        return res