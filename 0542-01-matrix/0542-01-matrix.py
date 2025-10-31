class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat),len(mat[0])

        dp = []

        visited = set()
        que = deque()

        for i in range(m):
            row = []
            for j in range(n):
                if mat[i][j]:
                    row.append(float("inf"))
                else:
                    row.append(0)
                    visited.add((i,j))
                    que.append((i,j))   
        
            dp.append(row)

        while que:
            l = len(que)

            for i in range(l):
                r,c = que.popleft()
                val = dp[r][c]
                if 0<=c-1<n and (r,c-1) not in visited:
                    dp[r][c-1] = val+1
                    visited.add((r,c-1))
                    que.append((r,c-1))
                if 0<=c+1<n and (r,c+1) not in visited:
                    dp[r][c+1] = val+1
                    visited.add((r,c+1))
                    que.append((r,c+1))
                if 0<=r-1<m and (r-1,c) not in visited:
                    visited.add((r-1,c))
                    dp[r-1][c] = val+1
                    que.append((r-1,c))
                if 0<=r+1<m and (r+1,c) not in visited:
                    visited.add((r+1,c))
                    dp[r+1][c] = val+1
                    que.append((r+1,c))
        return dp