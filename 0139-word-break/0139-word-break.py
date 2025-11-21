class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        def dictConstractS(ind):
            if ind == len(s):
                return True
            
            if ind in dp:
                return dp[ind]
            
            temp = False
            for word in wordDict:
                j = len(word)+ind
                if word == s[ind:j]:
                    temp|= dictConstractS(j)
            dp[ind] = temp
            return dp[ind]

        return dictConstractS(0)
                