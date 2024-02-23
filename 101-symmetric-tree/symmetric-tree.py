# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        return self.isMirror(root.left, root.right)

        
    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]):
            if not left and not right:
                return True
            if not left or not right:
                return False
            child1 =  self.isMirror(left.left, right.right)
            child2 = self.isMirror(left.right, right.left)
            return left.val == right.val and child1 and child2

        