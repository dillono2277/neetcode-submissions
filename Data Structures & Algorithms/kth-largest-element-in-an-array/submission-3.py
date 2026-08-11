class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []

        for num in nums:
            if len(minheap) < k:
                heapq.heappush(minheap, num)
            else:
                heapq.heappush(minheap, num)
                heapq.heappop(minheap)        
        return minheap[0]
