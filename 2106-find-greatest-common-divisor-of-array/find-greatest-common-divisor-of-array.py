class Solution:
    def findGCD(self, nums: List[int]) -> int:

        mn = nums[0]
        mx = nums[0]

        for i in nums:
            if i < mn:
                mn = i
            if i > mx:
                mx = i
        
        if (mx % mn) == 0:
            return mn
        
        gcd = 1

        for i in range(2, mn):
            if ((mn % i == 0) and (mx % i == 0)):
                gcd = i
        
        return gcd
