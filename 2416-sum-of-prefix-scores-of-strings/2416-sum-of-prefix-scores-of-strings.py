class TrieNode:
    def __init__ (self):
        self.children = [None for i in range(26)]
        self.count = 0

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        cur = self.root
        for char in word:
            ind = ord(char) - ord("a")
            if not cur.children[ind]:
                cur.children[ind] = TrieNode()
            cur.children[ind].count+=1
            cur = cur.children[ind]

    def count_score(self,word):
        cur = self.root
        count = 0
        for char in word:
            ind = ord(char) - ord("a")
            count+=cur.children[ind].count
            cur = cur.children[ind]
        return count
            

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        for word in words:
            self.insert(word)
        res = []
        for word in words:
            res.append(self.count_score(word))
        return res
