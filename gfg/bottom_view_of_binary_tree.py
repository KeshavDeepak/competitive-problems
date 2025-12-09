'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

from collections import deque

class Solution:
    def bottomView(self, root):
        queue = deque([(root, 0)])
        hd_to_val = {}
        
        while queue:
            # get next node and its hd
            node, hd = queue.popleft()
            
            # update hd_to_val
            hd_to_val[hd] = node.data
            
            # add children to queue
            if node.left:
                queue.append((node.left, hd-1))
            
            if node.right:
                queue.append((node.right, hd+1))
        
        # transform hd_to_val into an array
        answer = []
        
        for hd in sorted(hd_to_val.keys()):
            answer.append(hd_to_val[hd])
        
        #
        return answer
