class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # I gonna use k pointer and heap
        cols = {row:0 for row in range(len(nums))}

        # (val,index_of_kth list)
        mn_heap = []
        max_val = float('-inf')

        for r in range(len(nums)):
            max_val = max(max_val, nums[r][0])
            heapq.heappush(mn_heap,(nums[r][0], r))
        
        res = [mn_heap[0][0], max_val]

        while True:
            val,row = heapq.heappop(mn_heap)
            cols[row]+=1

            col = cols[row]
            if col >= len(nums[row]):
                break
            heapq.heappush(mn_heap, (nums[row][col], row))
        
            mn = mn_heap[0][0]
            max_val = max(max_val, nums[row][col])

            if max_val-mn < res[1]-res[0]:
                res = [mn,max_val]

        return res