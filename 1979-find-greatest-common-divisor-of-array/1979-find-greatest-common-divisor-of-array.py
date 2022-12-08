class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minNum = min(nums)
        maxNum = max(nums)
        divisor = None
        for i in range(maxNum, 0, -1):
            if maxNum % i == 0 and minNum % i == 0:
                divisor = i
                break
        
        return divisor