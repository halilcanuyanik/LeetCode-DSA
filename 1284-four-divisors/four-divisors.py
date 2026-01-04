class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for n in nums:
            divisors = set()
            for d in range(1, int(n ** (1/2) + 1)):
                if ((n % d) == 0):
                    divisors.add(d)
                    divisors.add(n // d)
                if len(divisors) > 4:
                    break
            if len(divisors) == 4:
                for d in divisors:
                    total += d
        return total