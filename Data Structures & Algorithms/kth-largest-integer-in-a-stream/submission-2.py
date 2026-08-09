import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #make the heap
        # make k a global variable
        self.maxheap = [-num for num in nums]
        heapq.heapify(self.maxheap)
        print(self.maxheap)
        self.k = k

        
    def add(self, val: int) -> int:
        #add val
        heapq.heappush(self.maxheap, -val)

        #make a copy, then loop through heap k -1 times to retrieve the kth largest
        heapcopy = list(self.maxheap)

        for i in range(self.k ):
            current = -heapq.heappop(heapcopy)
        
        return current



        
