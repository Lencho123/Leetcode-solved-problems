class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        heap = []
        max_heap = []
        visited_ind = set()
        wind = 0
        ans = 0
        for i in range(1,min(dist+2,len(nums))):
            heapq.heappush(heap,[nums[i],i])
        
        for i in range(k-1):
            val,ind = heapq.heappop(heap)
            heapq.heappush(max_heap,[-val,ind])
            visited_ind.add(ind)
            wind+=val

        ans = wind
        left = 1
        for right in range(dist+2,len(nums)):
            heapq.heappush(heap,[nums[right],right])
            cur_wind = wind
            
            while heap[0][1] <= left: #clean heap
                heapq.heappop(heap)
            while max_heap[0][1] <= left:#clean max_heap
                heapq.heappop(max_heap)

            if left in visited_ind:
                print(cur_wind, nums[left])
                print(cur_wind, heap[0][1])
                cur_wind-=nums[left]
                visited_ind.remove(left)

                while heap[0][1] <= left:
                    heapq.heappop(heap)
                
                val,ind = heapq.heappop(heap)

                heapq.heappush(max_heap,[-val,ind])
                cur_wind+=val
                visited_ind.add(ind)
            else:
                while heap[0][1] <= left: #clean heap
                    heapq.heappop(heap)
                while max_heap[0][1] <= left:#clean max_heap
                    heapq.heappop(max_heap)
                # check is the current intered element is smalles i.e it can make improvement by replacing
                if nums[right] < abs(max_heap[0][0]):
                    heapq.heappop(heap) #remove [nums[right],right]


                    valm,indm = heapq.heappop(max_heap) #pick max element from selected to replace it with new smaller element
                    visited_ind.remove(indm) #remove indm since it is not contributing to wind anymore
                    visited_ind.add(right) #add ind since it is contributing to wind anymore
                    cur_wind += -abs(valm) + nums[right]
                    heapq.heappush(heap,[abs(valm),indm]) #add -val,ind to cadidate heap for next try
                    heapq.heappush(max_heap,[-nums[right], right])

            left+=1
            wind = cur_wind
            ans = min(ans,cur_wind)

        return ans+nums[0]
