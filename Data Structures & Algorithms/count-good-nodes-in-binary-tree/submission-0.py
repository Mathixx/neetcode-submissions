# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = 0
        def dfs(node, curr_max):
            nonlocal count
            if node.val >= curr_max:
                curr_max = node.val
                count += 1
            
            if node.left:
                dfs(node.left, curr_max)
            if node.right:
                dfs(node.right, curr_max)
        
        dfs(root, float('-inf'))
        return count

            

