class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = collections.defaultdict(set)
        columnSet = collections.defaultdict(set)
        boxesSet = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                boxNumberRow = r // 3
                boxNumberCol = c // 3
                box = (boxNumberRow, boxNumberCol)

                if num in rowSet[r] or num in columnSet[c] or num in boxesSet[box]:
                    return False
                rowSet[r].add(num)
                columnSet[c].add(num)
                boxesSet[box].add(num)
        
 

        return True

        