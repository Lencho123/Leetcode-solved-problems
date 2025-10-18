class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remain_ind = defaultdict(list)

        for i,num in enumerate(arr):
            r = num%k
            needed = k-r
            if needed == k:
                needed = 0
            if needed in remain_ind and remain_ind[needed]:
                remain_ind[needed].pop()
            else:
                remain_ind[r].append(i)

        for r in remain_ind:
            if remain_ind[r]:
                return False
        return True