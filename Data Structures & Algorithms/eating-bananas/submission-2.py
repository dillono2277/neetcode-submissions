class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        
        l = 0
        r = max(piles)
        result = float('inf')

        def checkK(k : int) -> bool:
            if k  < 1:
                return False
            hoursTook = 0
            for pile in piles:
                hoursTook = hoursTook + math.ceil(pile / k)
            if hoursTook > h:
                return False
            return True
            


        while l <= r:
            k = (l + r) // 2
            if checkK(k):
                result = min(result, k)
                r = k - 1
            else:
                l = k + 1

        return result
        




        