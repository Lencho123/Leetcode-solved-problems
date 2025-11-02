class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = "9"*(len(pattern)+1)
        stack = []
        
        def backtrack(num,ind):
            nonlocal stack,res
            if len(stack) == len(pattern)+1:
                res = min(res,"".join(stack))
                return
            
            if pattern[ind] == "D":
                for i in range(1,num):
                    if str(i) not in stack:
                        stack.append(str(i))
                        backtrack(i,ind+1)
                        stack.pop()
            else:
                for i in range(num+1, 10):
                    if str(i) not in stack:
                        stack.append(str(i))
                        backtrack(i,ind+1)
                        stack.pop()

        for start in range(1, 10):
            stack = [str(start)]
            backtrack(start, 0)
            stack.pop()
        return res