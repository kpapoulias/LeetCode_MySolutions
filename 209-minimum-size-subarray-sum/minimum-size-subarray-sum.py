class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        min_length = float('inf')
        t_sum = 0

        for r in range(len(nums)):
            t_sum += nums[r]
            while t_sum >= target:
                min_length = min(min_length, r - l + 1)
                t_sum -= nums[l]
                l += 1
        
        if min_length < float('inf'):
            return min_length
        else:
            return 0