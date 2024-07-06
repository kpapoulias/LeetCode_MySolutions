class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []

        output = []
        start = nums[0]
        end = nums[0]

        for num in nums[1:]:
            if num == end + 1:
                end = num
            else:
                if start == end:
                    output.append("{}".format(start))
                else:
                    output.append("{}->{}".format(start, end))
                start = num 
                end = num

        if start == end:
            output.append("{}".format(start))
        else:
            output.append("{}->{}".format(start, end))

        return output