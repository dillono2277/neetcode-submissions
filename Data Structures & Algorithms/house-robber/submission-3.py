class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)

        for i in range(len(nums)):
            # maxMoney = max(maxMoney, (cache[i-2] + cache[i]))
            #first and second to first
            if i == 0:
                cache[i] = nums[i]
            elif i==1:
                cache[i] = max(cache[0], nums[i] )
            else:
                cache[i] = max(cache[i-1], cache[i-2] + nums[i])
        return cache[-1]
        
            



        