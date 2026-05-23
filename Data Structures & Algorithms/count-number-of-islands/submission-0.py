class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        def coverIsland(grid: List[List[str]], x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                return
            if grid[x][y] == "0":
                return
            else:
                grid[x][y] = "0"
            
                coverIsland(grid, x+1, y)  
                coverIsland(grid, x, y+1)
                coverIsland(grid, x-1, y)
                coverIsland(grid, x, y-1)



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands += 1
                    coverIsland(grid, i, j)
        return islands 

        