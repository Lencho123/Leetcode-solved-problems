class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = defaultdict(int)
        res = 0

        for a in answers:
            count[a]+=1
            if count[a] == a+1:
                res+=a+1
                # print(res)
                count[a] = 0

        for a in count:
            if count[a]:
                res+=a+1
        
        return res