from collections import deque

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        left = 0
        right = len(cells)-1
        answer = 0

        def isValidLandCell(grid, i, j):
            if 0 <= i < row and 0 <= j < col and grid[i][j] == 0:
                return True

            return False 

        while left <= right:
            curr = (left + right) // 2
            grid = [[0 for _ in range(col)] for _ in range(row)]
            
            # simulate water filling until current day
            for i,j in cells[:curr+1]:
                grid[i-1][j-1] = 1
            
            # multi-source bfs from top row to check if bottom row can be reached or not
            queue = deque([])
            visited = set()
            reached_bottom = False

            for j, cell in enumerate(grid[0]):
                if cell == 0: # land cell
                    queue.append((0, j))
                    visited.add((0, j))
            
            while queue:
                i, j = queue.popleft()

                # check if cell is on the bottom row or not
                if i == row-1: # hooray!
                    reached_bottom = True
                    break
                
                # append all of its unvisited land neighbors to queue
                for i_dir, j_dir in dirs:
                    nbr = (i+i_dir, j+j_dir)

                    if nbr not in visited and isValidLandCell(grid, nbr[0], nbr[1]):
                        queue.append(nbr)
                        visited.add(nbr)
            
            if reached_bottom: # found one solution, try finding a better day
                answer = curr
                left = curr + 1
            else: # could not find a solution, go left
                right = curr - 1
        
        return answer + 1
