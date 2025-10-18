class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        left, right = 1, x
        ans = 0
        while (left <= right):
            mid = left + (right - left) // 2
            if mid <= x // mid:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans