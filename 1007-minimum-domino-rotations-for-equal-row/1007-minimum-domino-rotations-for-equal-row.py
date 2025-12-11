class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        t_c = Counter(tops)
        b_c = Counter(bottoms)

        top_frequent = tops[0]
        bottom_frequent = bottoms[0]

        for i in range(len(tops)):
            if t_c[top_frequent] < t_c[tops[i]]:
                top_frequent = tops[i]
            if b_c[bottom_frequent] < b_c[bottoms[i]]:
                bottom_frequent = bottoms[i]
        
        b_flip_count = 0
        for i in range(len(tops)):
            if tops[i] != top_frequent:
                if bottoms[i] == top_frequent:
                    b_flip_count+=1
                else:
                    break
        
        t_flip_count = 0
        for i in range(len(bottoms)):
            if bottoms[i] != bottom_frequent:
                if tops[i] == bottom_frequent:
                    t_flip_count+=1
                else:
                    break

        res = float("inf")
        if t_flip_count+b_c[bottom_frequent] == len(tops):
            res = min(t_flip_count,res)
        if b_flip_count+t_c[top_frequent] == len(tops):
            res = min(b_flip_count,res)

        return -1 if res == float("inf") else res
