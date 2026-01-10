# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        new_node = Node(node.val)
        old_to_new = {node: new_node}
        queue = deque([node])

        while queue:
            curr_old = queue.popleft()
            curr_new = old_to_new[curr_old]

            # look through old neighbors and append/create accordingly
            for old_nbr in curr_old.neighbors:
                if old_nbr in old_to_new: # neighbor already exists in new graph
                    curr_new.neighbors.append(old_to_new[old_nbr])
                else: # neighbor doesn't exist yet, create placeholder new neighbor and append it to queue
                    new_nbr = Node(old_nbr.val)
                    old_to_new[old_nbr] = new_nbr

                    curr_new.neighbors.append(new_nbr)
                    queue.append(old_nbr)
        
        return new_node