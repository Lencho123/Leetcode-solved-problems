class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # I think i can use heap to solve this problem
        heap = [] #(val,ind)
        heapq.heappush(heap,(prices[0], 0))

        res = 0
        for i in range(1,len(prices)):
            res = max(prices[i]-heap[0][0], res)
            heapq.heappush(heap,(prices[i],i))
        return res