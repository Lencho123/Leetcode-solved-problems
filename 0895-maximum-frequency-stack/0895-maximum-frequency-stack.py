class FreqStack:

    def __init__(self):
        self.count = defaultdict(int)
        self.heap = [] #(freq,timestam,val)
        self.time = 0
        

    def push(self, val: int) -> None:
        self.count[val]+=1
        tupl = (-self.count[val],-self.time,val)
        heapq.heappush(self.heap, tupl)
        self.time+=1

    def pop(self) -> int:
        freq,time,val = heapq.heappop(self.heap)
        self.count[val]-=1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()