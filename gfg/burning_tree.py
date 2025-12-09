'''
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import deque

class Solution:
    def minTime(self, root, target):
        self.parent = {}
        self.target = None
        
        def dfs(root, parent):
            # base case
            if not root: return
        
            # update self.parent
            if parent:
                self.parent[root] = parent
            
            # if root is target, save it
            if root.data == target: self.target = root
            
            # recurse into children
            dfs(root.left, root)
            dfs(root.right, root)
        
        # populate self.parent
        dfs(root, None)
        
        # bfs from target node and keep track of time
        answer = -1
        queue = deque([self.target])
        visited = {None}
        
        while queue:
            nodes_in_curr_level = len(queue)
            
            for _ in range(nodes_in_curr_level):
                curr = queue.popleft()
                
                # add curr to visited
                visited.add(curr)
                
                # add all neighbors of curr if not visited yet
                if curr.left not in visited: queue.append(curr.left)
                if curr.right not in visited: queue.append(curr.right)
                if self.parent.get(curr, None) not in visited: queue.append(self.parent[curr])
            
            answer += 1
        
        #
        return answer


