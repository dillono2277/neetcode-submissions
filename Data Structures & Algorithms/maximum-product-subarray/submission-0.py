class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)

        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
            else:    
                temp = curMax * n
                curMax = max(n * curMax, n * curMin, n)
                curMin = min(temp, n * curMin, n)
                result = max(result, curMax, curMin)
        return result




        