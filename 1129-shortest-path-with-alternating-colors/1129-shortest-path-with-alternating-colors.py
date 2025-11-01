class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        ans = [float("inf") for i in range(n)]
        ans[0] = 0
        r_graph = defaultdict(list)
        b_graph = defaultdict(list)
        for u,v in redEdges:
            r_graph[u].append(v)

        for u,v in blueEdges:
            b_graph[u].append(v)

        def bfs():
            # red = 0, blue = 1 color
            visited = set([(-1,0)]) #(prev color, node)
            que = deque([(-1,0,0)]) ##(prev_color, node, distance)

            while que:
                pre_col,node,distance = que.popleft()

                if pre_col != 0:
                    for nei in r_graph[node]:
                        if (0,nei) not in visited:
                            ans[nei] = min(ans[nei], distance+1)
                            visited.add((0,nei))
                            que.append((0,nei,distance+1))
                if pre_col != 1:
                    for nei in b_graph[node]:
                        if (1,nei) not in visited:
                            ans[nei] = min(ans[nei], distance+1)
                            visited.add((1,nei))
                            que.append((1,nei,distance+1))
        bfs()

        for i,val in enumerate(ans):
            if val == float("inf"):
                ans[i] = -1
        return ans
                        