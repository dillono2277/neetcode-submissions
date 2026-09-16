class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        result = []

        def dfs(r, c, visited, prevHeight):
            if r >= rows or r < 0 or c >= cols or c < 0 or (r,c) in visited or heights[r][c] < prevHeight:
                return
            directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
            visited.add((r,c))

            for x, y in directions:
                dfs(r+x, c+y, visited, heights[r][c])


        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows-1][c])
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols-1])
        
        for r,c  in pacific:
            if (r,c) in atlantic:
                result.append([r,c])
        
        return result









        
        