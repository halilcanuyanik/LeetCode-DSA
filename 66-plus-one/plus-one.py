class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        number = 0
        new_digits = []

        for n in digits:
            number = number * 10 + n
        
        number += 1

        numStr = str(number)

        for n in numStr:
            new_digits.append(int(n))

        return new_digits

