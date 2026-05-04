# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_max = float("-inf")

        # Return max downards path sum that end in the node (node included)
        def dfs(node):
            nonlocal global_max
            if not node: return 0
            # Return max 
            left_path = dfs(node.left)
            right_path = dfs(node.right)

            max_path = node.val + max(0, left_path) + max(0, right_path)
            global_max = max(global_max, max_path)

            return max(node.val, node.val + max(left_path, right_path))

        dfs(root)

        return global_max
        