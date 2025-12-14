class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = []
        for i in range(len(s)):
            
            store = []
            if s[i] == ")":
                while stack and stack[-1] != "(":
                    store.append(stack.pop())
                if stack[-1] == "(":
                    stack.pop()
                    
                store = store[::-1]
                while store:
                    stack.append(store.pop())
            else:
                stack.append(s[i])
        return "".join(stack)