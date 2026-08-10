import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        result = []

        # making max heap of lenght k, if distance is less than top of maxheap, pop and add new  
        # distance    
        for i in range(len(points)):
            distance = math.sqrt(((points[i][0] - 0) ** 2) + ((points[i][1] - 0) ** 2))

            if len(maxheap) < k:
                heapq.heappush(maxheap, (-distance, points[i]))
            else:
                if distance < -maxheap[0][0]:
                    heapq.heappop(maxheap)
                    heapq.heappush(maxheap, (-distance, points[i]))
        
        while maxheap:
            output = heapq.heappop(maxheap)
            result.append(output[1]) # adding point
        return result 

        
            
        