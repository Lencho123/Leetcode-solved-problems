class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        absolute_sum = 0
        negative_count = 0
        min_num=abs(matrix[0][0])
        for i in range(n):
            for j in range(n):
                absolute_sum+=abs(matrix[i][j])
                negative_count+=matrix[i][j]<0
                min_num=min(min_num, abs(matrix[i][j]))

        print(min_num, negative_count, absolute_sum)
        if negative_count % 2 == 0:
            return absolute_sum
        else:
            return absolute_sum - 2*min_num
        