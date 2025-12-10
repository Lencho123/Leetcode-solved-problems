class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row,col = len(mat),len(mat[0])
        dirc = [[0,1],[1,0],[-1,0],[0,-1]]
        
        def in_bound(r,c):
            return 0<=r<row and 0<=c<col
        
        
        visited = set()
        que = deque()
        
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    visited.add((i,j))
                    que.append((i,j))
                    
            
        level = 0
        while que:
            l = len(que)
            
            for i in range(l):
                r,c = que.popleft()
                mat[r][c] = level
                for a,b in dirc:
                    if in_bound(r+a,c+b):
                        if (r+a,c+b) not in visited:
                            que.append((r+a,c+b))
                            visited.add((r+a,c+b))
                            
            level+=1
        return mat
                            
                            