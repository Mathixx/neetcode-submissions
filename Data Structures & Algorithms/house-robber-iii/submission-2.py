class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                # [rob_this_node, skip_this_node]
                return [0, 0]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 1. If we rob this node, we MUST NOT rob its children.
            # rob = current value + skip_left + skip_right
            rob = node.val + left[1] + right[1]
            
            # 2. If we skip this node, we can choose to either rob 
            # or skip each child (whichever yields more money).
            # skip = max(left_rob, left_skip) + max(right_rob, right_skip)
            skip = max(left) + max(right)
            
            return [rob, skip]

        # The answer is the best of the two choices at the root
        return max(dfs(root))
        