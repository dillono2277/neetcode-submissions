class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        seenGrid = [[0 for _ in row]for row in grid] 

        def coverIsland(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0


            if grid[i][j] == 0 or seenGrid[i][j] == 1:
                return 0
            
            seenGrid[i][j] = 1


            if grid[i][j] == 1:
                return (1 + coverIsland(grid, i+1, j) + 
                coverIsland(grid, i, j+1) + 
                coverIsland(grid, i-1, j) +
                coverIsland(grid, i, j-1))



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and seenGrid[i][j] == 0:
                    maxArea = max(maxArea, coverIsland(grid, i , j))
        
        return maxArea
        

         
        