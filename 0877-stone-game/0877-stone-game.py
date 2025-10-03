class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        res = 0
        dp = {}
        def dfs(turn, l, r):
            if l == r:
                return 0
            if (l,r) not in dp:
                if turn:
                    dp[(l,r)] =  max(piles[l] + dfs(~turn, l+1, r), piles[r] + dfs(~turn,l,r-1))
                else:
                    dp[(l,r)] = dfs(~turn, l+1, r) + dfs(~turn,l,r-1) 
            return dp[(l,r)]
        return dfs(True, 0, len(piles)-1) > sum(piles)/2