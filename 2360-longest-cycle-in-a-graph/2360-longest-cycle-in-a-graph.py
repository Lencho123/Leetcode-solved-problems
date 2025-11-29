class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        graph = defaultdict(list)
        incoming_count = defaultdict(int)

        for i,node in enumerate(edges):
            graph[i].append(node)
            incoming_count[node]+=1

        # Remove non cyclic node using topological sort
        not_cycle = set()
        que = deque()
        for i in range(len(edges)):
            if incoming_count[i] == 0:
                que.append(i)
                not_cycle.add(i)
        
        while que:
            l = len(que)
            for i in range(l):
                p = que.popleft()
                for nei in graph[p]:
                    incoming_count[nei]-=1
                    if incoming_count[nei] == 0:
                        que.append(nei)
                        not_cycle.add(nei)


        # i gonna track current step and store it in pre_tep hash
        res = -1
        pre_step = {}
        def dfs(node, cur_step):
            nonlocal res
            
            if node in pre_step: #Node has been visited
                res  = max(res, cur_step-pre_step[node])
                return

            pre_step[node] = cur_step
            for nei in graph[node]:
                dfs(nei,cur_step+1)
        
        for i in range(len(edges)):
            if i not in not_cycle:
                dfs(i,0)
        return res
                