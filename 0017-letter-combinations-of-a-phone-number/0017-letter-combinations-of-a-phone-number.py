class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dct = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno","7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        res = []
        def dfs(ind, s):
            if ind == len(digits):
                res.append(s)
                return
            for char in dct[digits[ind]]:
                dfs(ind+1,s+char)
            
        dfs(0,"")
        return res