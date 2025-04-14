# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.trackNode(root)
        return self.max_diameter

    def trackNode(self, root: Optional[TreeNode]) -> int:
        left_diameter, right_diameter = 0, 0
        if root.left:
            left_diameter = 1 + self.trackNode(root.left)
        if root.right:
            right_diameter = 1 + self.trackNode(root.right)

        self.max_diameter = max(self.max_diameter, left_diameter + right_diameter)

        return max(left_diameter, right_diameter)