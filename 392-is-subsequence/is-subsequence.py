class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ps = 0
        pt = 0

        while pt < len(t):
            if ps < len(s) and s[ps] == t[pt]:
                ps += 1
            pt += 1
            
        return ps == len(s)