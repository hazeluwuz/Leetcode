class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        
        res = [0] * len(temps)
        stack = []

        for idx, temp in enumerate(temps):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIdx = stack.pop()
                res[stackIdx] = (idx - stackIdx)
            stack.append([temp,idx])
        return res