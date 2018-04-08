"""
find the maximum subarray.

In the dp solution:
each time, we keep a array[i] to store the biggest subarray end(!!!) at i.

special case
consider the negative numbers and zero length
"""
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums):
            return 0

        k = 0
        sum = 0
        max = nums[0]
        for i in range(len(nums)):
            sum += nums[i]
            if sum < 0:
                sum = 0
                k = i
            if max < sum:
                max = sum
        return max

        