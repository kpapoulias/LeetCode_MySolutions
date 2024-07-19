class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        
        prefix_prod = 1
        for i in range(n):
            output[i] = prefix_prod
            prefix_prod *= nums[i]

        suffix_prod = 1
        for i in range(n-1, -1, -1):
            output[i] *= suffix_prod
            suffix_prod *= nums[i]

        return output