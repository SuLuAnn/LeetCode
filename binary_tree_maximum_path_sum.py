from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val
        def dfs(root: Optional[TreeNode]):
            nonlocal max_sum
            if not root:
                return 0
            left_max = dfs(root.left)
            right_max = dfs(root.right)
            max_sum = max(max_sum, left_max + right_max + root.val, left_max+ root.val, right_max + root.val, root.val)
            return max(root.val, left_max + root.val, right_max + root.val)
        dfs(root)
        return max_sum

if __name__ == "__main__":
    solution = Solution()
    result = solution.maxPathSum([73,74,75,71,69,72,76,73])
    print(result)