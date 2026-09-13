class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        for i in range(rows):
            for j in range(i+1, rows):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
        matrix[:] = [row[::-1] for row in matrix]

        