# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def updateResult(root: Optional[TreeNode],result):
            if root != None:
                updateResult(root.left,result)
                result.append(root.val)
                updateResult(root.right,result)

        updateResult(root,result)
        return result;

        