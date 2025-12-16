class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        
        stack = []
        hour = ""

        def backtrack(ind):
            nonlocal hour
            if len(stack) == 4:
                if int(str(arr[stack[0]])+str(arr[stack[1]])) < 24 and int(str(arr[stack[2]])+str(arr[stack[3]])) < 60:
                    hour = max(hour,str(arr[stack[0]])+str(arr[stack[1]])+":"+str(arr[stack[2]])+str(arr[stack[3]]))
                return
            
            for i in range(4):
                if i in stack:
                    continue
                stack.append(i)
                backtrack(i+1)
                stack.pop()
        backtrack(0)
        return hour if hour else ""