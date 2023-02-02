# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0 :
            return
        max_num = max(nums)
        max_idx = nums.index(max_num)
        node = TreeNode(max_num)
        if len(nums) > 1:
            node.left = self.constructMaximumBinaryTree(nums[0:max_idx])
            node.right = self.constructMaximumBinaryTree(nums[max_idx+1::])
            
        
        return node
        