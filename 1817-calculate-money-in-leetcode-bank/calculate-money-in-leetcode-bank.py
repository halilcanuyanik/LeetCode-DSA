class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        cur = 1
        total = 0
        while n > 0:
            for i in range(1,8):
                total += (i + cur - 1)
                n -= 1
                if n == 0:
                    break
            cur += 1
        return total