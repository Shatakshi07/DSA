# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # we go bottom up , calculate diameter of each node using its child node diameter.
        # max diam is max diam of left/right subtree + 1
        # diam and height both are used 
        # height helps for leaf node cases(-1 for where no node).
        diam=[0] #global variable

        def dfs(root):
            if not root:
                return -1  #height
            left_height = dfs(root.left)
            right_height = dfs(root.right)

            height = 1 + max(left_height , right_height)
            diam[0] = max(diam[0], left_height + right_height + 2)

            return height
            
        dfs(root)
        return diam[0]
