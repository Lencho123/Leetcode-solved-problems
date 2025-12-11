class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        count = 0
        for a in arr:
            count+= a == 0
        
        l = len(arr)-1
        r=len(arr)+count-1

        while l>=0:
            if arr[l] == 0:
                if r < len(arr):
                    arr[r] = 0
                if r-1 < len(arr):
                    arr[r-1] = 0
                r-=2
            else:
                if r<len(arr):
                    arr[r] = arr[l]
                r-=1
            l-=1