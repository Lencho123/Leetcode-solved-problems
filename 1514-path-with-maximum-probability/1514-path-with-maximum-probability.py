class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        for i,uv in enumerate(edges):
            u,v = uv
            graph[u].append((succProb[i],v))
            graph[v].append((succProb[i],u))
        
        probability = {i:0 for i in range(n)}
        probability[start_node] = 1

        heap = []
        heapq.heappush(heap,(-1,start_node))
        visited = set()

        while heap:
            fro_prob, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            if node == end_node:
                return abs(fro_prob)

            for to_prop, nei in graph[node]:
                probability[nei] = max(probability[nei], abs(fro_prob*to_prop))
                heapq.heappush(heap,(-abs(probability[nei]), nei))

        return float(0)