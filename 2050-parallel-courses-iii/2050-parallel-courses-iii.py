class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        graph = defaultdict(list)
        for u,v in relations:
            graph[u].append(v)
        
        dp = {}

        def dfs(node):
            if not graph[node]:
                return time[node-1]
            
            if node in dp:
                return dp[node]
            
            temp = 0
            for nei in graph[node]:
                temp = max(temp, time[node-1] + dfs(nei))
            dp[node] = temp
            return dp[node]
        
        res = 0
        for i in range(n):
            res = max(res, dfs(i+1))
        return res
