class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        available_on = {}
        time = 0

        for i, t in enumerate(tasks):
            time+=1
            if t in available_on:
                time = max(time, available_on[t])
            available_on[t] = time+space+1
        return time