class Solution(object):
    def strStr(self, haystack, needle):
            if not needle:
               return 0
            
            if len(needle) > len(haystack):
               return -1
            for i in range(len(haystack) - len(needle) + 1):
                if haystack[i:i+len(needle)] == needle:
                   return i
            return -1

    """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
