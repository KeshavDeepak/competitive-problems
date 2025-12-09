# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inorder_idx = {}
        self.pre_idx = 0

        # build inorder_idx
        for idx, val in enumerate(inorder):
            self.inorder_idx[val] = idx
        
        # recursive helper
        def helper(left, right):
            # base case
            if left > right: return

            # build root node
            root = TreeNode(preorder[self.pre_idx])
            self.pre_idx += 1

            # find index of root
            root_inorder_idx = self.inorder_idx[root.val]

            # connect root to left and right subtrees
            root.left = helper(left, root_inorder_idx-1)
            root.right = helper(root_inorder_idx+1, right)

            # 
            return root
        
        # 
        return helper(0, len(inorder)-1)
