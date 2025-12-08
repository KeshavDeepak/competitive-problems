# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = root.val

        # returns maximum path that ends at root
        def traverse(root) -> int:
            # base case
            if not root: return 0

            # find maximum left and right path
            maxi_left = max(traverse(root.left), 0)
            maxi_right = max(traverse(root.right), 0)

            # update self.maxi
            self.maxi = max(self.maxi, maxi_left + maxi_right + root.val)

            #
            return max(maxi_left, maxi_right) + root.val
        
        # traverse tree
        traverse(root)

        #
        return self.maxi
