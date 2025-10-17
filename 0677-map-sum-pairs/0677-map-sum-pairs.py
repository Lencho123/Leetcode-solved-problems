class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for i in range(26)]
        self.value = 0

class MapSum:

    def __init__(self):
        self.hashM = {}
        self.root = TrieNode()
        

    def insert(self, key: str, val: int) -> None:
        prev_val = 0
        if key in self.hashM:
            prev_val = self.hashM[key]

        self.hashM[key] = val
        val = val - prev_val

        cur = self.root
        for c in key:
            ind = ord(c) - ord("a")
            if not cur.children[ind]:
                cur.children[ind] = TrieNode()

            cur.children[ind].value+=val
            cur = cur.children[ind]

        cur.is_end = True

    def sum(self, prefix: str) -> int:
        cur = self.root
        sm = 0
        for c in prefix:
            ind = ord(c) - ord("a")
            if not cur.children[ind]:
                return 0
            cur = cur.children[ind]
        
        return cur.value
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)