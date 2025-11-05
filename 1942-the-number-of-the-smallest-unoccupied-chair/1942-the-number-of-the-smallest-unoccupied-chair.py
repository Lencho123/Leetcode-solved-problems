class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        for i in range(len(times)):
            times[i].append(i)
        
        times.sort()
        available = [i for i in range(len(times))]
        available_at = [] #(leave,table)

        heapq.heapify(available)

        for i,item in enumerate(times):
            coming_time,cur_leave,person = item

            while available_at and available_at[0][0] <= coming_time:
                leave, table = heapq.heappop(available_at)
                heapq.heappush(available, table)

            p = heapq.heappop(available)
            heapq.heappush(available_at,(cur_leave,p))
            
            if person == targetFriend:
                return p