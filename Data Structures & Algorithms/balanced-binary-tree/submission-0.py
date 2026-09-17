# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left = self.maxHeight(root.left)
        right = self.maxHeight(root.right)
        height = left - right
        if height < -1 or 1 < height:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))