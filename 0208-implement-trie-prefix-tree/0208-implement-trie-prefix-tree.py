class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            ind = ord(c)-ord('a')
            if not cur.children[ind]:
                cur.children[ind] = TrieNode()
            cur = cur.children[ind]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            ind = ord(c)-ord('a')
            if not cur.children[ind]:
                return False
            cur = cur.children[ind]

        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            ind = ord(c)-ord('a')
            if not cur.children[ind]:
                return False
            cur = cur.children[ind]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)