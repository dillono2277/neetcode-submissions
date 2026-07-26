# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(root, subRoot):
            if not root or not subRoot:
                return False
            if root.val == subRoot.val:
                if isEqual(root, subRoot) == True:
                    return True
            return dfs(root.left, subRoot) or dfs(root.right, subRoot)

        
        def isEqual(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            return True and isEqual(root.left, subRoot.left) and isEqual(root.right, subRoot.right)
        
        return dfs(root, subRoot)
            
