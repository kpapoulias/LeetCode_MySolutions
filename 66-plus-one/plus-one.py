class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # If the loop has ended without returning a result,
        # it means that all the digits in the array are '9'.
        # If all the digits are '9', prepend '1' to the array.
        return [1] + digits