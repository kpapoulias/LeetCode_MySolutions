class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i

            
    # for sorted (not descending) arrays
    def twoSumSorted(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = len(nums) - 1
        j = 0
        while j < i:
            l = nums[j]
            r = nums[i]

            if l + r == target:
                return [j, i]
            elif l + r < target:
                j += 1
            else:
                i -= 1