class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binarySearch(left: int, right: int, nums: List[int]):
            if left > right or right < left:
                return -1
            current = int((right + left) / 2)

            if nums[current] == target:
                return current
            elif nums[current] < target:
                return binarySearch(current+1, right, nums)
            else:
                return binarySearch(left, current-1, nums)

        return binarySearch(0, len(nums) - 1, nums)        