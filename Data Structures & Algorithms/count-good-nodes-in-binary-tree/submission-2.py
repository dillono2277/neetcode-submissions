# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.goodCount = 1
        parentSet = set()

        def dfs(root):
            if root is None:
                return None

            good = True
            for parent in parentSet:
                if root.val < parent.val:
                    good = False
                    break
            if good:
                self.goodCount += 1
            parentSet.add(root)
            dfs(root.left)
            dfs(root.right)
            parentSet.remove(root)


        
        # handle root
        parentSet.add(root)

        #left
        dfs(root.left)

        #clear set
        parentSet.clear()
        parentSet.add(root)


        #right
        dfs(root.right)

        return self.goodCount

        