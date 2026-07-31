class Solution:
    def rob(self, nums: List[int]) -> int:
        firstRob = 0
        secondRob = 0

        if len(nums) < 1:
            return -1
        if len(nums) == 1:
            return nums[0]

        def houseRob(nums):
            cache = [-1] * len(nums)

            for i in range(len(nums)):
                if i == 0:
                    cache[i] = nums[i]
                elif i == 1:
                    cache[i] = max(cache[0], nums[i])  
                else:   
                    cache[i] = max(cache[i-1], cache[i-2] + nums[i])  
            return cache[-1]

        firstRob = houseRob(nums[:-1])
        secondRob = houseRob(nums[1:])

        return max(firstRob, secondRob)