class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        shortest = min(strs, key=len)

        for i, char in enumerate(shortest):
            for remaining in strs:
                if remaining[i] != char:
                    return shortest[:i]

        return shortest