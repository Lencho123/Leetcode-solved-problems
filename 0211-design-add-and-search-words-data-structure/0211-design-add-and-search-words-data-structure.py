class TrieNode:
    def __init__(self):
        self.is_end = False
        self.is_leaf = True
        self.children = [None for i in range(26)]

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            ind = ord(c) - ord("a")
            if not cur.children[ind]:
                cur.children[ind] = TrieNode()
            cur = cur.children[ind]
        cur.is_end = True

    def search(self, word: str) -> bool:
        
        def dfs(node, index):
            if not node:
                return False

            if index == len(word):
                return node.is_end

            ind = ord(word[index]) - ord("a")

            temp = False
            if word[index] == ".":
                for i in range(26):
                    temp=temp or dfs(node.children[i],index+1)
            else:
                temp=temp or dfs(node.children[ind], index+1)
                
            return temp
            
        return dfs(self.root,0)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)