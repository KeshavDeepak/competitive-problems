from pprint import pprint 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

def display_tree(node, indent="", last=True):
        if node is not None:
            print(indent, end="")
            if last:
                print("└── ", end="")
                indent += "    "
            else:
                print("├── ", end="")
                indent += "│   "
            print(node.val)
            display_tree(node.left, indent, False)  # Left child is not last
            display_tree(node.right, indent, True)  # Right child is last

def lcaDeepestLeaves(root):
    pass
            
            

root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
print(lcaDeepestLeaves(root))
