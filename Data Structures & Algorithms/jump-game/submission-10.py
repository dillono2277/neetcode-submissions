class Solution:
    def canJump(self, nums: List[int]) -> bool: 
        maxReach = 0

        for i in range(len(nums)):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + nums[i])
        return True 

        # def check(i):
        #     if i >= len(nums) - 1:
        #         return True
        #     if nums[i] == 0:
        #         return False

        #     for j in range(1, nums[i] + 1):
        #         if check(i + j):
        #             return True
        #     return False

        # return check(0)
    