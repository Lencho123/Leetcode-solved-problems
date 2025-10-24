class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.is_end = False


class MagicDictionary:

    def __init__(self):
        self.root = TrieNode()

    def buildDict(self, dictionary: List[str]) -> None:
        def insert(word):
            cur = self.root
            for c in word:
                ind = ord(c) - ord("a")
                if not cur.children[ind]:
                    cur.children[ind] = TrieNode()
                cur = cur.children[ind]
            cur.is_end = True

        for word in dictionary:
            insert(word)

    def search(self, searchWord: str) -> bool:

        def is_in_dict(word):
            cur = self.root
            for c in word:
                ind = ord(c) - ord("a")
                if not cur.children[ind]:
                    return False
                cur = cur.children[ind]
            return cur.is_end

        replaced = searchWord
        for i in range(len(searchWord)):
            for j in range(26):
                new_char = chr(ord("a") + j)
                if new_char != searchWord[i]:
                    replaced = searchWord[:i] + new_char + searchWord[i+1:]
                    # check if single char replaced word is in dict
                    if is_in_dict(replaced):
                        return True
        
        return False
        
                
# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)