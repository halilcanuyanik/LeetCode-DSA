class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romans = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
        result = 0
        last_one = romans[s[-1]]
        for i in s[::-1]:
            if romans[i] < last_one:
                result -= last_one
                result += (last_one - romans[i])
            else :
                result += romans[i]
            last_one = romans[i]
        return result