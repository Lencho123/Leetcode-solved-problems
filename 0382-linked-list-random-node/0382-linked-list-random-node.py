# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.length = 0
        cur = self.head
        while cur:
            self.length+=1
            cur = cur.next


        # self.dct = {}#ind:val
        # dummy = ListNode(head)
        # prev = dummy
        # i = 0
        # while head:
        #     prev.next = None
        #     del prev
        #     prev = head 
        #     self.dct[i] = head.val
        #     i+=1
        #     head = head.next

        

    def getRandom(self) -> int:
        l = self.length
        ind = random.randrange(0,l,1)

        i = 0 
        cur = self.head
        while ind > 0:
            cur = cur.next
            ind-=1
        return cur.val

        # return self.dct[ind]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()