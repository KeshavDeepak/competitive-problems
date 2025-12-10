# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(root, key):
            if not root: # key not in tree
                return 

            if key == root.val: # root is key
                if root.left and root.right: # both children exist
                    # find inorder pred
                    pred = root.left

                    while pred.right:
                        pred = pred.right
                    
                    # swap pred's value into root
                    root.val = pred.val

                    # del pred 
                    root.left = delete(root.left, pred.val)

                    #
                    return root
                
                if root.left: # only left child exists
                    return root.left
                
                if root.right: # only right child exists
                    return root.right
                
                # no children (leaf node)
                return
            
            if key < root.val: # go left
                root.left = delete(root.left, key)
                return root

            if key > root.val: # go right
                root.right = delete(root.right, key) 
                return root
        
        return delete(root, key)


    
