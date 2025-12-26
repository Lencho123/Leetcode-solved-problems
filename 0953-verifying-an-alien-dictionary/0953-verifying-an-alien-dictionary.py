class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hash_val = {}
        
        for i,char in enumerate(order):
            hash_val[char] = chr(ord("a")+i)
        
        def gain(word):
            val = ""
            for char in word:
                val+=hash_val[char]
            return val
        
        ordered = sorted(words, key = lambda word: gain(word))
        return words == ordered