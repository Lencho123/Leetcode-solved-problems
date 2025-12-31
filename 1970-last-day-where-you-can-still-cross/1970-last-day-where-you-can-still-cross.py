from typing import List

class UnionFind:
    def __init__(self, rows, cols):
        self.parent = {(row, col): (row, col) 
                       for row in range(rows) 
                       for col in range(cols)}
        self.rank = {(row, col): 0 
                     for row in range(rows) 
                     for col in range(cols)}

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_p = self.find(x)
        y_p = self.find(y)
        if x_p == y_p:
            return

        # Union by rank
        if self.rank[x_p] < self.rank[y_p]:
            self.parent[x_p] = y_p
        else:
            self.parent[y_p] = x_p
            if self.rank[x_p] == self.rank[y_p]:
                self.rank[x_p] += 1

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        matrix = [[0]*col for _ in range(row)]
        dirc = [[0,1],[0,-1],[1,0],[-1,0]]

        def in_bound(r,c):
            return 0 <= r < row and 0 <= c < col

        # Fill all flooded cells
        for r, c in cells:
            matrix[r-1][c-1] = 1

        uf = UnionFind(row, col)

        # Virtual top and bottom nodes
        TOP = (-1,-1)
        BOTTOM = (-2,-2)
        uf.parent[TOP] = TOP
        uf.parent[BOTTOM] = BOTTOM
        uf.rank[TOP] = 0
        uf.rank[BOTTOM] = 0

        # Initial union of all water cells
        for r in range(row):
            for c in range(col):
                if matrix[r][c] != 0:
                    continue
                # Connect to neighbors
                for dr, dc in dirc:
                    rw, cl = r + dr, c + dc
                    if in_bound(rw, cl) and matrix[rw][cl] == 0:
                        uf.union((r,c),(rw,cl))
                        
                # Connect top/bottom virtual nodes
                if r == 0:
                    uf.union((r,c), TOP)
                if r == row-1:
                    uf.union((r,c), BOTTOM)

        res = len(cells)

        # If top and bottom already connected, return res
        if uf.find(TOP) == uf.find(BOTTOM):
            return res

        # Reverse add land back and check connectivity
        for i in range(1, len(cells)+1):
            r, c = cells[-i]
            r -= 1
            c -= 1
            matrix[r][c] = 0
            res -= 1

            # Union with neighbors
            for dr, dc in dirc:
                rw, cl = r + dr, c + dc
                if in_bound(rw, cl) and matrix[rw][cl] == 0:
                    uf.union((r,c), (rw, cl))

            # Connect to virtual top/bottom nodes
            if r == 0:
                uf.union((r,c), TOP)
            if r == row-1:
                uf.union((r,c), BOTTOM)

            if uf.find(TOP) == uf.find(BOTTOM):
                return res

        return res
