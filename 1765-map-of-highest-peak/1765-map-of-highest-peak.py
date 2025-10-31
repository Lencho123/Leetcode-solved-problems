class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        row, col = len(isWater), len(isWater[0])
        # res = []
        visited,que = set(),deque()

        for i in range(row):
            # rw = []
            for j in range(col):
                if isWater[i][j] == 1:
                    isWater[i][j] = 0
                    visited.add((i,j))
                    que.append((i,j))
                else:
                    isWater[i][j] = 1
        
        direction = [[1,0],[-1,0],[0,1],[0,-1]]

        while que:
            l  = len(que)
            
            for i in range(l):
                a,b = que.popleft()
                for dr,dc in direction:
                    r,c = dr+a,dc+b
                    if 0<=r<row and 0<=c<col and (r,c) not in visited:
                        isWater[r][c] = isWater[a][b]+1
                        visited.add((r,c))
                        que.append((r,c))
                        # print((r,c))
        return isWater