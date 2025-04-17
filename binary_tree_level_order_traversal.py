from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = []
        queue.append(root)
        while queue:
            cur_level = []
            tmp = []
            for node in queue:
                cur_level.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            ans.append(cur_level)
            queue = tmp
        return ans
if __name__ == "__main__":
    solution = Solution()
    result = solution.levelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))
    print(result)


