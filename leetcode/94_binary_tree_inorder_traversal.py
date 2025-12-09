# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        answer = []

        while curr:
            if curr.left:
                # find predecessor
                pred = curr.left

                while pred.right and pred.right != curr:
                    pred = pred.right
                
                # if pred is already attached, then left subtree is done
                if pred.right == curr:
                    pred.right = None
                    answer.append(curr.val)
                    curr = curr.right
                else: # if not, then attach it and go to the left subtree
                    pred.right = curr
                    curr = curr.left
            else:
                answer.append(curr.val)
                curr = curr.right
        
        return answer

  
