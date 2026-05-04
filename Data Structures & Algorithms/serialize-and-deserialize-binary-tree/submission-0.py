# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res = ""
        stack = [root]
        while stack:
            new_stack = []
            for node in stack:
                if not node or node==None:
                    res += "_" + ","
                else:
                    res += str(node.val) + ","
                    new_stack.append(node.left)
                    new_stack.append(node.right)
            stack = new_stack
        return res

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        else:
            nodes = data.split(",")
            n = len(nodes) - 1
            root = TreeNode(val=int(nodes[0]))
            
            level = [root]
            next_level = []
            i = 1
            while level and i < n:
                for node in level:
                    if nodes[i] != "_":
                        node.left = TreeNode(val=int(nodes[i]))
                        next_level.append(node.left)
                    i+=1
                    
                    if nodes[i] != "_":
                        node.right = TreeNode(val=int(nodes[i]))
                        next_level.append(node.right)
                    i+=1
                
                level = next_level
            
            return root
