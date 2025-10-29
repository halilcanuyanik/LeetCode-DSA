class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        e_str = ""
        ans = 0
        idx = 0
        while n != 0:
            n = n // 2
            ans += (2 ** (idx))
            idx += 1
        return ans
        
        