# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        max_val, min_val = 0, 0
        if p.val > q.val:
            max_val = p.val
            min_val = q.val
        else:
            max_val = q.val
            min_val = p.val
        while root:
            if root.val > max_val:
                root = root.left
            elif root.val < min_val:
                root = root.right
            else:
                return root
        

