class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        numberDic = dict()
        n = len(nums) / 2
        for i in nums:
            if i in numberDic:
                if numberDic[i] == n - 1:
                    return i
                numberDic[i] += 1
            else:
                numberDic[i] = 1
        for k in numberDic:
            if numberDic[k] == n:
                return k
            else:
                continue
        