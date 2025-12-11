from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        unvisited = set()

        islands = 0

        # populate unvisited
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    unvisited.add((i, j))
                    
        # choose each unvisited node and bfs 
        while unvisited:
            source = unvisited.pop()
            queue = deque([source])

            # bfs on source
            while queue:
                i, j = queue.popleft()

                # add all land neighbours
                left = (i, max(j-1, 0))
                if left in unvisited:
                    unvisited.remove(left)
                    queue.append(left)
                
                up = (max(i-1, 0), j)
                if up in unvisited:
                    unvisited.remove(up)
                    queue.append(up)
                
                right = (i, min(j+1, m))
                if right in unvisited:
                    unvisited.remove(right)
                    queue.append(right)
                
                down = (min(i+1, n), j)
                if down in unvisited:
                    unvisited.remove(down)
                    queue.append(down)
                
            # one island found
            islands += 1
        
        #
        return islands

        
