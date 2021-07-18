class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for i in range(n//2):
            for j in range((n+1)//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = temp
        
# (n-1-j, i) -> (i, j)


# another way is doing transpose first and then reflect:
# 1 2 3     9 6 3     7 4 1
# 4 5 6  -> 8 5 2  -> 8 5 2
# 7 8 9     7 4 1     9 6 3

