# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def buildNode(preorder, inorder):
            if not preorder:
                return None
            root_val = preorder[0]
            root = TreeNode(val=root_val)

            left_size = 0
            while inorder[left_size] != root_val:
                left_size += 1
            
            root.left = buildNode(preorder[1:1+left_size], inorder[:left_size])
            root.right = buildNode(preorder[1+left_size:], inorder[left_size+1:])

            return root
        
        return buildNode(preorder, inorder)
            
        