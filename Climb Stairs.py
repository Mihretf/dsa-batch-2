class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        a=1
        b=2
        for i in range(3, n+1):
            a,b= b, a+b
        return b
        """
        :type n: int
        :rtype: int
        """
        
