class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.is_end = False
        self.word = None  #  ADD this to store the full word


class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insertWord(self, word):
        cur = self.root
        for char in word:
            ind = ord(char) - ord("a")
            if not cur.children[ind]:
                cur.children[ind] = TrieNode()
            cur = cur.children[ind]
        cur.is_end = True
        cur.word = word  #  Store full word here
        return
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        b_row, b_col = len(board), len(board[0])
        dirc = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def in_bound(r,c):
            return 0 <= r < b_row and 0 <= c < b_col
        

        trie = Trie()
        res = set()
        for word in words:
            trie.insertWord(word)

        #  REMOVE curWord parameter completely
        def backtrack(row, col, curNode):
            
            ind = ord(board[row][col]) - ord("a")
            temp = board[row][col]
            board[row][col] = "#"  #  mark visited

            if not curNode.children[ind]:
                board[row][col] = temp
                return
            
            nxt = curNode.children[ind]

            #  Use word from Trie node instead of curWord
            if nxt.word:
                res.add(nxt.word)
                nxt.word = None  # avoid duplicates

            # Explore all four directions
            for i,j in dirc:
                nr, nc = row+i, col+j
                #  simplified DFS condition: remove (row+i,col+j) check
                if in_bound(nr, nc) and board[nr][nc] != "#":
                    backtrack(nr, nc, nxt)
                    
            board[row][col] = temp  #  restore character
            
        for i in range(b_row):
            for j in range(b_col):
                backtrack(i, j, trie.root)  #  no curWord parameter
                
        return list(res)
