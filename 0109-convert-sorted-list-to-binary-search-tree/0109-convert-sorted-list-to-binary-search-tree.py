# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        LIST = []
        while head:
            LIST.append(head.val)
            head=head.next
        
        def constructBST(start, end):
            if start > end:
                return None
            
            mid = (start + end)//2
            root = TreeNode(LIST[mid])
            root.left = constructBST(start,mid-1)
            root.right = constructBST(mid+1,end)
            return root
            
        return constructBST(0,len(LIST)-1)