class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        richer_graph = defaultdict(list)
        for rich,poor in richer:
            richer_graph[poor].append(rich)
        dp = {}

        def dfs(poor_node):
            if poor_node in dp:
                return dp[poor_node]

            temp = poor_node
            for rich in richer_graph[poor_node]:
                node = dfs(rich)
                if quiet[temp] > quiet[node]:
                    temp = node
            dp[poor_node] = temp
            return dp[poor_node]
        
        ans = []
        for node in range(len(quiet)):
            ans.append(dfs(node))
        return ans