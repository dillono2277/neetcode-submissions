class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        def dfs(i):
            if i >= n:
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            robCurrent = nums[i] + dfs(i+2)
            robSkip = dfs(i+1)
            dp[i] = max(robCurrent, robSkip)

            return dp[i]
        
        return dfs(0)
        

