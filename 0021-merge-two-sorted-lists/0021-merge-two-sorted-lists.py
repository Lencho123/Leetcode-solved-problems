# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        merged = ListNode()
        ptr = merged

        while list1 and list2:
            node = None
            if list1.val < list2.val:
                node = ListNode(list1.val)
                list1 = list1.next
            else:
                node = ListNode(list2.val)
                list2 = list2.next
            ptr.next = node
            ptr = ptr.next
        
        if list1:
            ptr.next = list1
        else:
            ptr.next = list2
        return merged.next
    