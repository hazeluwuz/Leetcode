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
            queue_len = len(queue)
            for i in range(queue_len):
                node = queue.pop(0)
                if node.left is not None:
                    print(node.left.val)
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            if len(queue): 
                nodes.append(queue[-1].val)
        return nodes
