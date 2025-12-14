# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        while root:
            if not root.left:
                root = root.right 
                continue

            # find inorder pred
            pred = root.left

            while pred.right:
                pred = pred.right
            
            # connect pred to right
            pred.right = root.right

            # 
            root.right = root.left
            root.left = None

            root = root.right

        
