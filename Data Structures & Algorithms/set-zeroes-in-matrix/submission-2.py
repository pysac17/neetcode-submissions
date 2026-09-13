class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        row_flag, col_flag = False, False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    if r==0:
                        row_flag = True
                    if c==0:
                        col_flag = True
                    elif r!=0 and c!=0:
                        matrix[r][0] = 0
                        matrix[0][c] = 0
        
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if row_flag:
            matrix[0] = [0]*cols
        if col_flag:
            for i in range(rows):
                matrix[i][0] = 0

                    