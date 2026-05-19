class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        if n > 1:
            cache[0] = 1
            cache[1] = 2
        else:
            return 1
        for i in range(2, n):
            cache[i] = cache[i-1] + cache[i-2]
        return cache[n-1]

        # cache = [-1] * n
        # def dfs(i):
        #     if i >= n:
        #         return i == n # 1 if we reached n, 0 if we went passed
        #     if cache[i] != -1:
        #         return cache[i]
        #     cache[i] =  dfs(i+1) + dfs(i+2)
        #     return cache[i]
        
        # return dfs(0)

        