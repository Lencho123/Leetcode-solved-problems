class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        '''
        [[4,3,2,-1],
         [3,2,1,-1],
         [1,1,-1,-2],
         [-1,-1,-2,-3]]

         start (0,col-1)
         if the cell is < 0 take all num below it col wise is negative, so add row-r+1 and then move to left i.e c+1
         else: move down row wise i.e r+1
        '''
        res = 0
        row,col = len(grid),len(grid[0])
        r,c = 0,col-1

        while c >= 0 and r < row:
            if grid[r][c] < 0:
                res+=row-r
                c-=1
            else:
                r+=1
        return res