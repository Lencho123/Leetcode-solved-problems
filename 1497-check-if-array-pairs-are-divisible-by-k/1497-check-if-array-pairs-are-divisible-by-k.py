class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        isTaken = [False for i in range(len(arr))]

        remainders = defaultdict(list)
        pairs = []
        for i,num in enumerate(arr):
            x = num%k
            y = (k - x)%k
            if y in remainders and len(remainders[y]):
                ind = remainders[y].pop()
                isTaken[ind] = True
                isTaken[i] = True
                pairs.append((arr[i],arr[ind]))
            else:
                remainders[x].append(i)
        
        
        if sum(isTaken) == len(arr):
            return True
        return False