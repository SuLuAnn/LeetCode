import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root: Optional[TreeNode], maximum: int, minimum: int ) -> bool:
            if not root:
                return True
            return root.val < maximum and root.val > minimum \
                and dfs(root.left, root.val, minimum) \
                and dfs(root.right, maximum, root.val)
        
        return dfs(root.left, root.val, -sys.maxsize - 1) and dfs(root.right, sys.maxsize, root.val)

