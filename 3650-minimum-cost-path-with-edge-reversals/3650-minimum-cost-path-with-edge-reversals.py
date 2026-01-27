class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u,v,w in edges:
            graph[u].append([v,w])
            graph[v].append([u,2*w])

        distance = {i:float("inf") for i in range(n)}
        distance[0] = 0

        heap = []#(w,node)
        heapq.heappush(heap,(0,0))
        visited = set()

        while heap:
            w,node = heappop(heap)
            visited.add(node)
            for nei,wei in graph[node]:
                if nei not in visited:
                    if wei + w < distance[nei]:
                        distance[nei] = wei + w
                    heapq.heappush(heap,(distance[nei],nei))
        return distance[n-1] if distance[n-1] != float("inf") else -1


