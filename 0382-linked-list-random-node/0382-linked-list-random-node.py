# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.dct = {}#ind:val
        i = 0
        while self.head:
            self.dct[i] = self.head.val
            i+=1
            self.head = self.head.next
        

    def getRandom(self) -> int:
        l = len(self.dct)
        ind = random.randrange(0,l,1)
        return self.dct[ind]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()