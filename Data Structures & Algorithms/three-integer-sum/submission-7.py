class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []


        for i in range(len(nums)):
            target = -(nums[i])
            left = i+1
            right = len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right]
                if nums[left] + nums[right] == target:
                    if [nums[i], nums[left], nums[right]] not in output:
                        output.append([nums[i], nums[left], nums[right]])
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return output


        