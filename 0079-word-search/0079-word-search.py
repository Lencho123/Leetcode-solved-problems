class TrieNode:
    def __init__(self):
        self.children = {char:None for char in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root
        for ch in word:
            if not cur.children[ch]:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.is_end = True

            


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        directions = [[1,0],[0,1], [-1,0], [0,-1]]
        
        def search(r,c,node):
            if not(0 <= r < row and 0 <= c < col) or (r,c) in visited:
                return False
            
            ch = board[r][c]
            if not node.children[ch]:
                return False
            
            if node.children[ch].is_end:
                return True
            
            visited.add((r,c))
            for dr,dc in directions:
                if search(r+dr,c+dc, node.children[ch]):
                    return True
            visited.remove((r,c))
            return False

            
        
        trie = Trie()
        trie.insert(word)
        for i in range(row):
            for j in range(col):
                visited = set()
                if search(i,j,trie.root):
                    return True
        return False