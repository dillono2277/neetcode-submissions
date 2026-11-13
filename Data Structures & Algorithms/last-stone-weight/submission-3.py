import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop_max(stones)
            stone2 = heapq.heappop_max(stones)
            print("stone1: ", stone1)
            print("stone2: ", stone2)
            if stone1 == stone2:
                continue
            else:
                heapq.heappush_max(stones, stone1 - stone2)
            print("result", stones)
        if len(stones) > 0:
            return heapq.heappop_max(stones)
        else:
            return 0



        