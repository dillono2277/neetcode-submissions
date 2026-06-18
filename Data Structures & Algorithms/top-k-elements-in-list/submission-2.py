class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqArr = [[] for i in range(len(nums) + 1)]
        count = {}
        result = []

        for num in nums:
            if num in count:
                count[num] +=1
            else:
                count[num] = 1

        for num, freq in count.items():
            freqArr[freq].append(num)

        
        for i in range(len(freqArr) -1, -1, -1):
            for n in freqArr[i]:
                result.append(n)
                if len(result) == k:
                    return result
        return []

        