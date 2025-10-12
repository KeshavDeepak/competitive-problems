from typing import Optional
import copy


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return copy.deepcopy(node) # hehe
            
            

#helper function
def build_graph(adj_list):
    nodes = {}
    # Create all nodes
    for i in range(1, len(adj_list)+1):
        nodes[i] = Node(i)
    # Add neighbors
    for idx, neighbors in enumerate(adj_list):
        nodes[idx+1].neighbors = [nodes[n] for n in neighbors]
    return nodes[1]

# main code
solution = Solution()

# test cases
adj_list = [[2,4],[1,3],[2,4],[1,3]]
first_node = build_graph(adj_list)
print(solution.cloneGraph(first_node))