class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        temp = sorted(nums)
        if temp == nums or temp == nums[::-1]: return True
        return False