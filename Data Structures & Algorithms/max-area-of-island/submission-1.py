class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        def coverIsland(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0


            if grid[i][j] == 0:
                return 0
            

            if grid[i][j] == 1:
                grid[i][j] = 0
                return (1 + coverIsland(grid, i+1, j) + 
                coverIsland(grid, i, j+1) + 
                coverIsland(grid, i-1, j) +
                coverIsland(grid, i, j-1))



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, coverIsland(grid, i , j))
        
        return maxArea
        

         