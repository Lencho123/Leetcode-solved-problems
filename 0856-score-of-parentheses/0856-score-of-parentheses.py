class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for i,char in enumerate(s):
            if char == "(":
                stack.append(0)
            else:
                p = stack.pop()
                p = max(1,2*p)
                stack[-1]+=p
        return stack[-1]