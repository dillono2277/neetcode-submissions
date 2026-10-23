class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixDict = {0:1} # prefixSum : count
        curSum = 0

        for r in range(len(nums)):
            curSum += nums[r]
            target = curSum - k
            if target in prefixDict:
                res += prefixDict[target]
            
            if curSum in prefixDict:
                prefixDict[curSum] += 1
            else:
                prefixDict[curSum] = 1
        return res

            

        