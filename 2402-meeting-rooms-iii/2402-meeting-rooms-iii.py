class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        count = defaultdict(int)
        max_val = -1

        available_rooms = []
        for i in range(n):
            heapq.heappush(available_rooms,i)

        available_time = [] #(av_time, room)

        for start,end in meetings:
            gap = end-start
            while available_time and start >= available_time[0][0]:
                av_time,room = heapq.heappop(available_time)
                heapq.heappush(available_rooms, room)
            
            smallest_room = 0
            if available_rooms:
                smallest_room = heapq.heappop(available_rooms)
            else:
                av_time, room = heapq.heappop(available_time)
                start = av_time
                end = start+gap
                smallest_room = room
            
            heapq.heappush(available_time,(end,smallest_room))
            count[smallest_room]+=1
            max_val = max(max_val,count[smallest_room])
        

        res = n-1
        for room in count:
            if count[room] == max_val:
                res = min(room, res)
        return res