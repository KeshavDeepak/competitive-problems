# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def get_inorder(root):
            if not root: return []

            return get_inorder(root.left) + [root] + get_inorder(root.right)
        
        # get inorder
        inorder = get_inorder(root)

        # two pointer approach
        left = 0
        right = len(inorder) - 1

        while left < right:
            curr_sum = inorder[left].val + inorder[right].val
            
            if k == curr_sum:
                return True
            elif k > curr_sum:
                left += 1
            else: # k < curr_sum
                right -= 1
        
        #
        return False

        
