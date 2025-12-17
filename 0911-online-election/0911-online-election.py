class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.prewin = []
        self.freq_hash = defaultdict(int)
        self.heap = [] #(-freq,-timestap,person)
        
        
        for i in range(len(self.times)):
            self.freq_hash[persons[i]]+=1
            heapq.heappush(self.heap,(-self.freq_hash[persons[i]], -times[i], persons[i]))
            self.prewin.append(self.heap[0][-1])

    def q(self, t: int) -> int:
        index = bisect_right(self.times, t)-1
        if index < 0:
            return 0
        return self.prewin[index]
        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)