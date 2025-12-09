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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        stay = root
        while stay:
            p1 = stay
            p2 = stay.left
            
            if p2:
                p2.next = p1.right
                p2 = p2.next
                
            while p1 and p2:
                p1 = p1.next
                p2.next = p1.left if p1 else None
                p2 = p2.next
                if p2:
                    p2.next = p1.right if p1 else None
                    p2 = p2.next
            stay = stay.left
        return root