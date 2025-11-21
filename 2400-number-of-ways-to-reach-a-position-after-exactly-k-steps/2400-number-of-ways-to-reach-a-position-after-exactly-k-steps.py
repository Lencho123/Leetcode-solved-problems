class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        dp = {}
        MOD = 10**9 + 7
        def countWays(pos,left_steps):
            if left_steps == 0:
                if pos == endPos:
                    return 1
                return 0
            
            if (pos,left_steps) in dp:
                return dp[(pos,left_steps)]
            
            left = countWays(pos-1, left_steps-1)%MOD
            right = countWays(pos+1, left_steps-1)%MOD
            dp[(pos,left_steps)] = (left + right)%MOD
            return dp[(pos,left_steps)]
        return countWays(startPos, k)