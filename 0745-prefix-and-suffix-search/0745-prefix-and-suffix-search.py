class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for i in range(26)]
        self.indices = set()


class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.rev_words = [word[::-1] for word in words]
        self.root = TrieNode()
        self.rev_root = TrieNode()

        # construct tries for frist initializatio
        for ind,word in enumerate(self.words):
            self.insert(word, False, ind)
        
        for ind,word in enumerate(self.rev_words):
            self.insert(word, True, ind)

    def insert(self,word, reverse, index):
        cur = self.root
        if reverse:
            cur = self.rev_root
        
        for c in word:
            ind = ord(c) - ord("a")
            if not cur.children[ind]:
                cur.children[ind] = TrieNode()
            cur.children[ind].indices.add(index)
            cur = cur.children[ind]
        cur.is_end = True
    
    def check_pre_suf(self, persuf, is_suf):
        cur = self.root
        if is_suf:
            cur = self.rev_root
        
        for c in persuf:
            ind = ord(c) - ord("a")
            if cur and not cur.children[ind]:
                return set()
            if cur:
                cur = cur.children[ind]
        return cur.indices


    def f(self, pref: str, suff: str) -> int:

        pre_inds = list(self.check_pre_suf(pref, False))
        pre_inds.sort(reverse = True)

        suf_inds = self.check_pre_suf(suff[::-1], True)


        res = -1 
        for i in pre_inds:
            if i in suf_inds:
                return i
                res = max(res,i)
        
        return -1
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)    
