class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goalIndex = n - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goalIndex:
                goalIndex = i
            
            
        if goalIndex == 0:
            return True
        return False




















        # i = 0
        # while i < len(nums) - 1:
        #     if nums[i] == 0:
        #         return False
        #     nextMax = 0
        #     nextInd = 0
        #     for j in range(i+1, (i + nums[i]) + 1):
        #         if nums[j] == 0:
        #             if j == len(nums) - 1:
        #                 return True
        #             else:
        #                 continue
        #         if nums[j] >= (len(nums)- 1) - j:
        #             i = j
        #             break
        #         else:
        #             nextMax = max(nextMax, nums[j])
        #             if nums[j] > nextMax:
        #                 nextInd = j
        #     i += j
        # return True


        