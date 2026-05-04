# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
    
        def dfs(root, parent_robbed):
            # Returns the max amount of money robbed starting form root
            # Knowing your parents house has ben robbed or not
            if not root:
                return 0
            
            if (root, parent_robbed) in memo:
                return memo[(root, parent_robbed)]
        
            if parent_robbed:
                # You can't rob anyway
                val = dfs(root.left, False) + dfs(root.right, False)
                memo[(root, parent_robbed)] = val
                return val
            else:
                robbing = dfs(root.left, True) + dfs(root.right, True)
                not_robbing = dfs(root.left, False) + dfs(root.right, False)
                val = max(robbing + root.val, not_robbing)
                memo[(root, parent_robbed)] = val
                return val

        return dfs(root, False)
        