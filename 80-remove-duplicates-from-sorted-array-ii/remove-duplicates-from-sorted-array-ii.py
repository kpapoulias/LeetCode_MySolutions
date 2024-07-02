class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0

        for i in nums:
            if count < 2 or i != nums[count - 2]:
                nums[count] = i
                count += 1
        return count