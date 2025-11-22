class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] - stones[0] != 1:
            return False
        
        ind_of = {}
        for i,stone in enumerate(stones):
            ind_of[stone] = i
        
        dp ={}

        def jump(pos,step):
            if pos in ind_of and ind_of[pos] == len(stones)-1:
                return True

            if (pos,step) in dp:
                return dp[(pos,step)]

            temp = False
            if pos in ind_of:
                if step > 1:
                    temp|=jump(pos+step-1, step-1)
                temp|=jump(pos+step,step)
                temp|=jump(pos+step+1,step+1)

            dp[(pos,step)] = temp
            return dp[(pos,step)]


        return jump(stones[1],1)