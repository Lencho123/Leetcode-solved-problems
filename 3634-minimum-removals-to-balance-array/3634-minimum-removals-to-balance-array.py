class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        min_heap = nums[:]
        max_heap = [-nums[i] for i in range(len(nums))]

        heapq.heapify(min_heap)
        heapq.heapify(max_heap)

        count = 0
        while True:
            if -max_heap[0] <= min_heap[0]*k:
                return count
            count+=1
            heapq.heappop(max_heap)
