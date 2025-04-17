# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        if root == p:
            return p
        if root == q:
            return q
        cur_left = self.lowestCommonAncestor(root.left, p, q)
        cur_right = self.lowestCommonAncestor(root.right, p, q)
        if cur_left and cur_right:
            return root
        return cur_left or cur_right
