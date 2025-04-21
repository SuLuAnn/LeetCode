from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stored = []
        def dfs(root: TreeNode, k: int, stored: list):
            if root and len(stored) < k:
                dfs(root.left, k, stored)
                if len(stored) < k:
                    stored.append(root.val)
                dfs(root.right, k, stored)
        dfs(root, k, stored)
        return stored[-1]
            
    
if __name__ == "__main__":
    solution = Solution()
    result = solution.kthSmallest(TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6)), 3)
    print(result)
        