class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        stack = []

        def backtrack(op,cl):
            if op == cl == n:
                res.append("".join(stack[:]))
                return
            
            if op > cl:
                stack.append(")")
                backtrack(op,cl+1)
                stack.pop()
            if op < n:
                stack.append("(")
                backtrack(op+1,cl)
                stack.pop()
        backtrack(0,0)
        return res