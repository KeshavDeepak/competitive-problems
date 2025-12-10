# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # both nodes are in the right subtree
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # both nodes are in the left subtree
        if p.val < root.val and q.val < root.val: 
            return self.lowestCommonAncestor(root.left, p, q)

        # either root is one of the two nodes or the nodes are in differing subtrees
        return root
