class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxSequence = 0
        for num in nums:
            if num - 1 not in numSet:
                #findSequence
                curSequence = 1
                curNum = num
                while curNum + 1 in numSet:
                    curSequence += 1
                    curNum += 1
                maxSequence = max(maxSequence, curSequence)
        return maxSequence

        