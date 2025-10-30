class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        count = Counter(tasks)
        maxHeap = [-i for i in count.values()]
        heapq.heapify(maxHeap) #task_count

        que = deque() #(task_count, idle_time)

        while maxHeap or que:
            time+=1

            if maxHeap:
                p = heapq.heappop(maxHeap)
                p+=1
                if p:
                    que.append((p,time+n))
            if que and que[0][1] <= time:
                heapq.heappush(maxHeap,que.popleft()[0])

        return time