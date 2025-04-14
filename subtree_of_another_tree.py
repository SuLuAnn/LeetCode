from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        targetDepth = self.trackDepth(subRoot)
        records = []
        self.trackTragetDepth(root, targetDepth, records)
        for record in records:
            if self.isSameTree(record, subRoot):
                return True
        return False

    def trackDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.trackDepth(root.left), self.trackDepth(root.right))
    
    def trackTragetDepth(self, root: Optional[TreeNode], targetDepth: int, records: list) -> int:
        if not root:
            return 0
        
        curDepth = 1 + max(self.trackTragetDepth(root.left, targetDepth, records), self.trackTragetDepth(root.right, targetDepth, records))
        if curDepth == targetDepth:
            records.append(root)
        return curDepth
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)