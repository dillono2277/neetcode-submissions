# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(root):
            if root is None:
                return 0
            if root.left and root.right:
                return 1 + max(dfs(root.left), dfs(root.right))
            elif root.left:
                return 1 + dfs(root.left)
            else:
                return 1 + dfs(root.right)
        return dfs(root)
        