class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        count = {}
        
        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        vals = count.values()
        
        return len(set(vals)) == len(vals)