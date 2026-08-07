class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #start to end method

        # dp = [1] * len(nums)

        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)

        # bottom up method
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, - 1, -1):
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

        