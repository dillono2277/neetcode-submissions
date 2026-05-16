import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # initalize k and heap
        # heap is only k length of last elements of nums
        self.k = k
        self.heap = []

        for num in nums:
            heapq.heappush(self.heap, num)
        


        
        

    def add(self, val: int) -> int:
        # insert val into heap
        heapq.heappush(self.heap, val)
        #heapify heap after pusing val
        heapq.heapify(self.heap)
        # if heap is bigger than k , pop to make it k size
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

        #heapify heap after popping items
        heapq.heapify(self.heap)
        
        return self.heap[0]
        
           

