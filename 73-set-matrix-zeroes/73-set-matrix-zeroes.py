class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # loop over the matrix, storing any zero's location
        row_zeros = set()
        col_zeros = set()

        for row_idx, row in enumerate(matrix):
            for col_idx, col in enumerate(row):
                if matrix[row_idx][col_idx] == 0:
                    row_zeros.add(row_idx)
                    col_zeros.add(col_idx)

        for row_idx, row in enumerate(matrix):
            for col_idx, col in enumerate(row):
                if row_idx in row_zeros or col_idx in col_zeros:
                    matrix[row_idx][col_idx] = 0

        return matrix