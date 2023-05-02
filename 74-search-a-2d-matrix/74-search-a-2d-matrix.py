class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for x in range(len(matrix) - 1, -1, -1):
            row = matrix[x]
            if row[0] > target:
                continue
            if row[-1] < target:
                continue
            for j in range(len(row)):
                if row[j] > target:
                    continue
                cur_item = matrix[x][j]
                if cur_item == target:
                    return True
        return False