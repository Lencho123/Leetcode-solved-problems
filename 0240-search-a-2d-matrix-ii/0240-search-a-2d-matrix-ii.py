class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def bin_search(arr, t):
            l,r = 0,len(arr)-1
            while l <= r:
                m = l + (r-l)//2
                if t > arr[m]:
                    l = m+1
                elif t < arr[m]:
                    r = m-1
                else:
                    return True
            return False
    
        for row in matrix:
            if bin_search(row, target):
                return True
        return False