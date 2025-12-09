"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        que = deque()
        if root:
            que.append(root)
        ans = []
        while que:
            l = len(que)
            nex = None
            level = []
            
            for i in range(l):
                node = que.popleft()
                node.next = nex
                
                nex = node
                if node.right:
                    que.append(node.right)
                if node.left:
                    que.append(node.left)
            ans.append(level[::-1])
        return root