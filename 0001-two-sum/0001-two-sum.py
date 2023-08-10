class Solution:
    def twoSum(self, nums, target):
        dct = {}
        for i, num in enumerate(nums):
            cur_num = target - num
            if cur_num in dct:
                return [dct[cur_num], i]
            dct[num] = i
        return []