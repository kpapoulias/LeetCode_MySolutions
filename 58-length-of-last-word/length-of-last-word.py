class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = s.rstrip().rsplit(" ", 1)
        # improved but does not run on leetcode code editor
        # x = s.rsplit(maxsplit = 1)
        return(len(x[-1]))
        