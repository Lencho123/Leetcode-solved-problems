class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for i in range(26)]


class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.longest = ""



    def insert(self, word):
        cur = self.root
        for c in word:
            ind = ord(c) - ord("a")
            if not cur.children[ind]:
                cur.children[ind] = TrieNode()

            # cur.count=cur.count+1

            cur = cur.children[ind]
        cur.is_end = True
        
    
    def longestWord(self, words: List[str]) -> str:
        # words = sorted(words)
        for word in words:
            self.insert(word)

        longest = ""
        def dfs(node, cand):
            nonlocal longest
            if len(cand) > len(longest) or (len(cand) == len(longest) and cand < longest):
                longest = cand

            for i in range(26):
                if node.children[i] and node.children[i].is_end:
                    dfs(node.children[i], cand+chr(i + ord("a")))
        
        for i in range(26):
            child = self.root.children[i]
            if child and child.is_end:
                dfs(child, chr(i+ord("a")))

        return longest