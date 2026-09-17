# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + self.helper(root.left,root.val) + self.helper(root.right,root.val) 

    def helper(self, root: TreeNode, counter: int) -> int:
        if not root:
            return 0
        if root.val >= counter:
            counter = root.val
            return 1 + self.helper(root.left,counter) + self.helper(root.right,counter) 
        return self.helper(root.left,counter) + self.helper(root.right,counter) 