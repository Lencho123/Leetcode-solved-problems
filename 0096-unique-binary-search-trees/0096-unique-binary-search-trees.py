class Solution:
    def numTrees(self, n: int) -> int:
        dp = {0:1}

        for node in range(1,n+1):
            node_total = 0
            for root in range(1,node+1):
                left = root-1
                right = node - root
                node_total+=dp[left]*dp[right]
            dp[node] = node_total
        return dp[n]