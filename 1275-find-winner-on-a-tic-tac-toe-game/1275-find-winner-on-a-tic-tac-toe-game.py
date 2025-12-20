class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[0 for i in range(3)] for i in range(3)]
        
        i = 0
        for r,c in moves:
            if i%2 == 0:
                grid[r][c] = "A"
            else:
                grid[r][c] = "B"
            i+=1
        
        def checkright(i,j):
            if i != 0:
                return False
            return grid[i][j] == grid[i+1][j] == grid[i+2][j]
        
        def checkbottom(i,j):
            if j != 0:
                return False
            return grid[i][j] == grid[i][j+1] == grid[i][j+2]
        
        def checkdiag(i,j):
            if i == j == 0:
                return grid[i][j] == grid[i+1][j+1] == grid[i+2][j+2]
            if i == 0 and j == 2:
                return grid[i][j] == grid[i+1][j-1] == grid[i+2][j-2]
            return False
        
        for i in range(3):
            for j in range(3):
                if (checkright(i,j) or checkbottom(i,j) or checkdiag(i,j)) and grid[i][j]:
                    return grid[i][j]
        
        if len(moves) == 9:
            return "Draw"
        print(grid)
        return "Pending"