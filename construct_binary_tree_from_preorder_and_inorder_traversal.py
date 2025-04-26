from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder = deque(preorder)
        root = self.granNode(preorder, inorder)

        return root
    
    def granNode(self, preorder: deque, inorder: List[int]) -> Optional[TreeNode]:
            if not inorder or not preorder:
                return None
            value = preorder.popleft()

            i = inorder.index(value)
            left = self.granNode(preorder, inorder[0:i])
            right = self.granNode(preorder, inorder[i+1:])
            return TreeNode(value, left, right)
            
if __name__ == "__main__":
    Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])