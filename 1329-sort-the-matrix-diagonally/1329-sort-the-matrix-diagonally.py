class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row,col = len(mat),len(mat[0])
        diag_inds = defaultdict(list)
        
        for r in range(row):
            for c in range(col):
                diag_inds[r-c].append(mat[r][c])
        
        visited_diag = set()
        for r in range(row):
            for c in range(col):
                if r-c in visited_diag:
                    break
                
                visited_diag.add(r-c)
                leng = min(row-r, col-c)
                diag_inds[r-c].sort()
                for l in range(leng):
                    mat[r+l][c+l] = diag_inds[r-c][l]
        return mat