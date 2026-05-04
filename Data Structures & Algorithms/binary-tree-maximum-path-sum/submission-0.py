# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_path_sum = float("-inf")
        def dfs_ps(node):
            # Returns the only descending max path sum
            nonlocal max_path_sum
            if not node:
                return 0
            else:
                maxLeft = dfs_ps(node.left)
                maxRight = dfs_ps(node.right)
                max_path_sum = max(max_path_sum, max(maxLeft, 0) + node.val + max(maxRight, 0))
                
                return node.val + max(max(maxLeft, maxRight), 0)
        
        dfs_ps(root)
        return max_path_sum

        