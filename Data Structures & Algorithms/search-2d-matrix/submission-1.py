class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix[0]) - 1

        for i in range(len(matrix)):
            if matrix[i][r] < target or matrix[i][l] > target:
                continue
            else:
                while l<=r:
                    curr = l + (r-l) // 2
                    if matrix[i][curr] == target:
                        return True
                    elif matrix[i][curr] < target:
                        l = curr+1
                    else:
                        r = curr-1
        return False

