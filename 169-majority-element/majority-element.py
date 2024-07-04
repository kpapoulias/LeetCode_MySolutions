from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_counter = Counter(nums)
        num_of_common_el = my_counter.most_common(1)[0][1]
        if (num_of_common_el > len(nums) // 2):
            return my_counter.most_common(1)[0][0]
        
    def majorityElement2(self, nums):
        m = {}
        for n in nums:
            m[n] = m.get(n, 0) + 1
            if (m[n] > len(nums) // 2):
                return n

    def majorityElement3(self, nums):
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate