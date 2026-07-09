class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def findTargetRow(left: int, right: int):
            if left > right:
                return -1
            middleRow = (right + left) // 2
            if matrix[middleRow][-1] >= target and matrix[middleRow][0] <= target:
                return middleRow
            elif matrix[middleRow][0] > target:
                return findTargetRow(left, middleRow - 1)
            else:
                return findTargetRow(middleRow + 1, right)
        def findTarget(row: int, left: int, right: int):
            if left > right:
                return False
            middle = (right + left) // 2
            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] > target:
                return findTarget(row, left, middle - 1)
            else:
                return findTarget(row, middle+1, right)


        if len(matrix) == 1:
            return findTarget(0, 0, len(matrix[0]) - 1)
        if len(matrix) < 1:
            return False

        targetRow = findTargetRow(0, len(matrix) - 1)
        if targetRow == -1:
            return False
        return findTarget(targetRow, 0, len(matrix[targetRow]) - 1)
        






        


        