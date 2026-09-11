from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        mins = 0

        def checkFruit(row, col):
            if row >= rows or row < 0 or col >= cols or col < 0 or grid[row]  [col] == 2 or grid[row][col] == 0:
                return 0

            q.append((row, col))
            grid[row][col] = 2
            return 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
        
        while len(q) > 0:
            currentRotts = []
            while len(q):
                currentRotts.append(q.popleft())
            
            for rottRow, rottCol in currentRotts:
                checkFruit(rottRow + 1, rottCol)
                checkFruit(rottRow, rottCol + 1)
                checkFruit(rottRow - 1, rottCol)
                checkFruit(rottRow, rottCol -1)

            if len(q) > 0:
                mins += 1
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return mins






        