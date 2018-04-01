class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping = dict()
        for ix in range(len(nums)):
            num = nums[ix]
            mapping[num] = ix 
        new_num = sorted(nums)
        i = 0
        j = len(nums) - 1
        
        while i < j:
            num1 = new_num[i] 
            num2 = new_num[j]
            if num1 + num2 > target:
                j -= 1
            elif num1 + num2 < target:
                i += 1
            else:
                break

        # need to consider the case there isn't any match
        ret = []
        for k in range(len(nums)):
            if nums[k] == new_num[i] or nums[k] == new_num[j]:
                ret.append(k)
        return ret



