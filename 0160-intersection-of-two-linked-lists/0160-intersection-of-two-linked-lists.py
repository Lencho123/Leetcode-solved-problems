# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA, lenB=0,0
        currA=headA
        currB=headB
        # find lenA
        while currA:
            lenA+=1
            currA=currA.next

        # find lenB
        while currB:
            lenB+=1
            currB=currB.next
        
        # check longer list
        count1, count2=0,0
        if lenA>lenB:
            longer=headA
            shorter=headB
            while longer:
                if lenA-count1>lenB:
                    count1+=1
                    longer=longer.next
                    continue
                if longer==shorter:
                    skipA=count1
                    skipB=count2
                    return longer
                count1+=1
                count2+=1
                shorter=shorter.next
                longer=longer.next
        else:
            longer=headB
            shorter=headA
            while longer:
                if lenB-count1>lenA:
                    count1+=1
                    longer=longer.next
                    continue
                if longer==shorter:
                    skipA=count2
                    skipB=count1
                    return longer
                count2+=1
                count1==1
                shorter=shorter.next
                longer=longer.next
        return None       