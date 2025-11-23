class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
         
        graph = defaultdict(set)
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        que = deque()
        for i in range(n):
            if len(graph[i]) == 1:
                que.append(i)

        root1,root2 = None,None
        while que:
            root1 = None
            root2 = None

            l = len(que)
            for i in range(l):
                p = que.popleft()
                if root1 != None:
                    root2 = p
                else:
                    root1 = p
                
                for nei in graph[p]:
                    graph[nei].remove(p)
                    if len(graph[nei]) == 1:
                        que.append(nei)
        res = []
        if root1 != None:
            res.append(root1)
        if root2 != None:
            res.append(root2)
            
        return res
                    
                    