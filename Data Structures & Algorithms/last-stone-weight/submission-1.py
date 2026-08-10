import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-stone for stone in stones]
        heapq.heapify(maxheap)

        while len(maxheap) > 1:
            x = -heapq.heappop(maxheap)
            y = -heapq.heappop(maxheap)
            if x == y:
                continue
            else:
                newStone = x - y
                heapq.heappush(maxheap, -newStone)
        
        if len(maxheap) >= 1:
            return -heapq.heappop(maxheap)
        else:
            return 0

            
        