class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        count=0
        right=0
        for i in arr:
            if i==0:
                count+=1

        while right < (len(arr)):
            if arr[right]==0:
                arr.insert(right+1,0)
                right+=2
            else:
                right+=1

        for i in range(count):
            arr.pop()
        print(arr)
        print(count)