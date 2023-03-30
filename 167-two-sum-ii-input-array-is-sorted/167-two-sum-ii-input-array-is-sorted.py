class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # initialize two pointers
        left = 0
        right = len(numbers) - 1

        # loop until left and right pointers meet
        while left < right:

                # get the sum of the two numbers
                sum = numbers[left] + numbers[right]

                # if sum is equal to target, return the indices
                if sum == target:
                    return [left + 1, right + 1]

                # if sum is greater than target, decrement right pointer
                elif sum > target:
                    right -= 1

                # if sum is less than target, increment left pointer
                else:
                    left += 1

        # if no solution found, return empty list
        return []