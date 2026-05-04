# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        diameter = 0

        def dfs_depth(root):
            nonlocal diameter
            if not root.left and not root.right:
                return 1
            else:
                maxLeft = dfs_depth(root.left) if root.left else 0
                maxRight = dfs_depth(root.right) if root.right else 0
                diameter = max(diameter, maxLeft + maxRight)
                return max(maxLeft, maxRight) + 1
        
        dfs_depth(root)

        return diameter
        