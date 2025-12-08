# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def traverse(root):
            # base case
            if not root: return -1

            # find left and right heights
            left_height = traverse(root.left)
            right_height = traverse(root.right)

            # find biggest diameter of root and update global diameter
            self.diameter = max(self.diameter, left_height + right_height + 2)

            # 
            return max(left_height, right_height) + 1
        
        traverse(root)

        return self.diameter
