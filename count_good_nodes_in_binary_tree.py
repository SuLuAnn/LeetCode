class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return 1 + self.dfs(root.left, root.val) + self.dfs(root.right, root.val)
    
    def dfs(self, root: TreeNode, maximum: int) -> int:
        if root:
            cur = 0
            if maximum <= root.val:
                cur = 1
                maximum = root.val
            return cur + self.dfs(root.left, maximum) + self.dfs(root.right, maximum)
        return 0
