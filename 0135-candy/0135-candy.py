class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [0]*n
        
        heap = []
        for i,r in enumerate(ratings):
            heapq.heappush(heap,(r,i))
        
        while heap:
            rate,ind = heappop(heap)
            left_cand = candies[ind-1] if ind > 0 and ratings[ind-1]<rate else 0
            right_cand = candies[ind+1] if ind < n-1 and ratings[ind+1] < rate else 0

            candies[ind] = max(left_cand,right_cand)+1
        return sum(candies)