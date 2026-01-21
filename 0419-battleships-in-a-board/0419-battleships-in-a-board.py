class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        row,col = len(board),len(board[0])
        
        def dfs(r,c):
            nonlocal flag
            if 0<=r+1<row and 0<=c+1<col and board[r][c] == board[r][c+1] == board[r+1][c] == "X":
                flag = False
            board[r][c] = "."
            
            for dr,dc in [[0,1],[1,0]]:
                if r+dr < row and c+dc < col and board[r+dr][c+dc] == "X":
                    dfs(r+dr,c+dc)
        
        res = 0
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == "X":
                    flag = True
                    dfs(r,c)
                    res+=flag
        return res
                
                    