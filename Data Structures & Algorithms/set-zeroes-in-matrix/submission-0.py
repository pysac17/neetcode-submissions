class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        zero_arr = set()
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_arr.add((i,j))

        for r, c in zero_arr:
            matrix[r] = [0] * cols
            for i in range(rows):
                matrix[i][c] = 0