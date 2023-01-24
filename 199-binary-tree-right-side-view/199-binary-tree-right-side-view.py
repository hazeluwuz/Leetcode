# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = [root]
        nodes = [root.val]
        while(len(queue) > 0):
            test = []
            queue_len = len(queue)
            for i in range(queue_len):
                temp = queue.pop(0)
                if temp.left is not None:
                    print(temp.left.val)
                    queue.append(temp.left)
                if temp.right is not None:
                    queue.append(temp.right)
            if len(queue): 
                nodes.append(queue[-1].val)
        return nodes
