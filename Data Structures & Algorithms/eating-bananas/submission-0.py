class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        minK = float('inf')

        #temp hours = ceil(piles[i] / k)
        while left <= right:
            k = (right + left) // 2
            totalHours = 0
            for pile in piles:
                totalHours = totalHours + math.ceil(pile / k)
            if totalHours <= h:
                right = k - 1
                minK = min(minK, k)
            else:
                left = k + 1
        return minK






        