class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix = []
        postfix = []
        
        preProduct = 1
        for i in range(len(nums)):
            preProduct = preProduct * nums[i]
            prefix.append(preProduct)

        postProduct = 1
        for i in range(len(nums) -1, -1, -1):
            postProduct = postProduct * nums[i]
            postfix.append(postProduct)
        postfix.reverse()
        
        for i in range(len(nums)):
            if i == 0:
                output.append(postfix[i+1])
            elif i == len(nums) - 1:
                output.append(prefix[i-1])
            else:
                output.append(prefix[i-1] * postfix[i+1])
        return output
        