class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix ={}
        suffix = {}

        #find prefix
        curPref = 1
        for i in range(len(nums)):
            prefix[i] = curPref
            curPref = curPref * nums[i]

        #find suff
        curSuf = 1
        for i in range(len(nums) -1, -1, -1):
            num = nums[i]
            suffix[i] = curSuf
            curSuf = curSuf * num

        # multiply both together into result
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])
        return result

