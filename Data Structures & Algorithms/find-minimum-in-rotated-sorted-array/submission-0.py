class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r = len(nums) - 1
        result = float('inf')

        while l <= r:
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break
            mid = (l + r) // 2
            result = min(result, nums[mid])

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return result

            
        