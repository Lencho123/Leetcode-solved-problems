class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((w,v))

        distance = {i:float("inf") for i in range(1,n+1)}
        distance[k] = 0
        visited = set()

        heap = []
        heapq.heappush(heap, [0,k])

        while heap:
            weigh,fro_node = heapq.heappop(heap)

            if fro_node in visited:
                continue
            visited.add(fro_node)
            
            for wei,nei in graph[fro_node]:
                if distance[nei] > distance[fro_node] + wei:
                    distance[nei] = distance[fro_node] + wei
                
                heapq.heappush(heap,[distance[nei],nei])
          
        return max(distance.values()) if max(distance.values()) < float("inf") else -1
