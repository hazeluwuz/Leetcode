class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i in range(len(nums)):
            cur_num = nums[i]
            remainder = target - cur_num
            if remainder in dct:
                return [i, dct[remainder]]
            dct[cur_num] = i
        return None
