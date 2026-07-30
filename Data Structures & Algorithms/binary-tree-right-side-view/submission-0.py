# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        result = []

        queue.append(root)

        while queue:
            queueLen = len(queue)
            level = []
            for i in range(queueLen):
                current = queue.popleft()
                if current:
                    level.append(current)
                    queue.append(current.left)
                    queue.append(current.right)
            if level:
                result.append(level[-1].val)
        return result
            
        
        