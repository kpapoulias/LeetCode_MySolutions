from collections import Counter

class Solution(object):
    def canConstruct(self, s, t):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # initial solution
        sCounter = Counter(s)
        tCounter = Counter(t)

        for i in sCounter.keys():
            if i not in tCounter or sCounter[i] > tCounter[i]:
                return False
        return True
    
        # 2nd way: using set properties (intersection: &)
        # if sCounter & tCounter == sCounter:
        #     return True
        # return False