class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        reversed_graph = defaultdict(list)
        for u,v in edges:
            reversed_graph[v].append(u)
        
        dp = {}
        def dfs(node):
            if node in dp:
                return dp[node]
            res = set()
            for par in reversed_graph[node]:
                res.add(par)
                res.update(dfs(par))
            dp[node] = res
            return dp[node]
        ans = []
        for node in range(n):
            ans.append(sorted(list(dfs(node))))

        return ans