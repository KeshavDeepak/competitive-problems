# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            # base case
            if not root: return

            # is root one of the search nodes?
            if root == p or root == q:
                return root
            
            # if not, then find search nodes in both subtrees
            left = dfs(root.left)
            right = dfs(root.right)

            # if both subtrees contain each one of the nodes, then root is current lca
            if left and right:
                return root
            
            # if only one of the subtrees contain one of the nodes, then that is current lca
            if left: return left
            if right: return right

            # if none of the subtrees contained any of the nodes, return null
            return None

        # 
        return dfs(root)
