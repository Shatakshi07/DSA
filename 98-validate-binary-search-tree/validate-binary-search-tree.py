# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node , leftboundary , rightboundary):
            if not node:
                return True
            if not (node.val < rightboundary and node.val > leftboundary):
                return False

            return( valid(node.left , leftboundary , node.val) and
                    valid(node.right , node.val , rightboundary))

        return valid(root , float("-inf") , float("inf"))

        