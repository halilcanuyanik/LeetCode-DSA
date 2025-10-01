class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 1
        size = len(nums)
        while idx < size:
            if (nums[idx - 1] == nums[idx]):
                nums.pop(idx)
                size -= 1
            else:
                idx += 1
        return len(nums)