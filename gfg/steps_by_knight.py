from collections import deque

class Solution:
	def minStepToReachTarget(self, knightPos, targetPos, n):
		queue = deque([tuple(knightPos)])
		visited = set()
		layer = 0
		
		while queue:
		    curr_length = len(queue)
		    
		    for _ in range(curr_length):
		        curr = queue.popleft()
		        
		        if curr in visited:
		            continue
		       
		        visited.add(curr)
		        
		        if list(curr) == targetPos:
		            return layer
		        
		        paths = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]
		        
		        for path in paths:
		            dest = (curr[0] + path[0], curr[1] + path[1])
		            
		            if 1 <= dest[0] < (n+1) and 1 <= dest[1] < (n+1):
		                queue.append(dest)
            
            layer += 1
        
        return -1
