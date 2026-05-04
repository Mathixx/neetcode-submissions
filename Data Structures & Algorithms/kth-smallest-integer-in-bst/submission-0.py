# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Lets implement inorder traversal

        def inorder(node):
            if not node: return []
            else:
                return inorder(node.left) + [node.val] + inorder(node.right)
        
        trav = inorder(root)
        return trav[k-1]
        