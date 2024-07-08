class Solution(object):
    # initial solution
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        s_letterCount = {}
        t_letterCount = {}

        for char_s, char_t in zip(s, t):
            s_letterCount[char_s] = s_letterCount.get(char_s, 0) + 1
            t_letterCount[char_t] = t_letterCount.get(char_t, 0) + 1
            
        return s_letterCount == t_letterCount
    
    # optimized solution: reducing the number of iterations through the strings by using a single dictionary
    def isAnagramOptimized(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        letterCount = {}

        for char in s:
            letterCount[char] = letterCount.get(char, 0) + 1

        for char in t:
            if char in letterCount:
                letterCount[char] -= 1
                if letterCount[char] == 0:
                    del letterCount[char]
            else:
                return False
        return len(letterCount) == 0