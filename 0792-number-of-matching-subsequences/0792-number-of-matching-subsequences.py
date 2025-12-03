class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        indices = defaultdict(list)

        for i,char in enumerate(s):
            indices[char].append(i)
        
        def is_match(indices, word):
            ind = -1
            for w in word:
                if w not in indices: return 0

                ind_lst = bisect_right(indices[w], ind)
                if ind_lst == len(indices[w]):
                    return 0
                ind = indices[w][ind_lst]
            return 1
            

        res = 0
        for word in words:
            res+=is_match(indices,word)
        
        return res