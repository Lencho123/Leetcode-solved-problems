class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heappush(heap, (0,-1)) #(presum, ind)
        pre_sum = 0
        res = float("inf")
        for i,n in enumerate(nums):
            pre_sum+=n
            dif = pre_sum - k

            while heap and heap[0][0] <= dif:
                sm,ind = heapq.heappop(heap)
                res = min(res,i-ind)

            heapq.heappush(heap,(pre_sum,i))
            

        return res if res != float("inf") else -1