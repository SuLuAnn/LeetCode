from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        records = []
        records.append(root)
        ans = []
        while records:
            is_level_exist = False
            tmp = []
            for node in records:
                if node:
                    tmp.append(node.right)
                    tmp.append(node.left)
                    if not is_level_exist:
                        ans.append(node.val)
                        is_level_exist = True
            records = tmp
        return ans
