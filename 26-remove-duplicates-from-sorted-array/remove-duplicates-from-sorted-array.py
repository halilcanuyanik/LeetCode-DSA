class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 0
        size = len(nums)
        while idx < size:
            if ((idx != 0) and (nums[idx - 1] == nums[idx])):
                nums.pop(idx)
                size -= 1
            else:
                idx += 1
        return len(nums)