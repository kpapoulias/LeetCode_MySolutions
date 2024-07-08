class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n > 1 and n not in seen:
            seen.add(n)
            n = self.squareSum(n)
        return n == 1

    def squareSum(self, n):
        s = 0
        while n > 0:
            s += (n % 10) ** 2
            n = n // 10
        return s