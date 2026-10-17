class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0 for _ in range(n)] for _ in range(m)]

        #initilaize last row:
        for c in range(n):
            cache[m-1][c] = 1

        #initlaize last col
        for r in range(m):
            cache[r][n-1] = 1

        for r in range(m - 2, -1 , -1):
            for c in range(n - 2, -1, -1):
                cache[r][c] = cache[r+1][c] + cache[r][c+1]
        return cache[0][0]


        