import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = [-num for num in nums]

        heapq.heapify(maxheap)

        for i in range(k):
            result = -heapq.heappop(maxheap)
        return result






        