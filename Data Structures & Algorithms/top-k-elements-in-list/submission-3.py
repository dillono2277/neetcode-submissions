from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = Counter(nums)
        countDict = sorted(countDict.items(), key=lambda item: item[1], reverse=True)
        res = []

        temp = 0
        for num, count in countDict:
            if temp == k:
                return res
            res.append(num)
            temp += 1
        return res

        