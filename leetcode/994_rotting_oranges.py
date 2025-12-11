from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        queue = deque()

        n = len(grid)
        m = len(grid[0])

        answer = 0

        # find count of fresh oranges and add rotten oranges to a queue
        for i in range(n):
            for j in range(m):
                cell = grid[i][j]

                if cell == 1:
                    fresh += 1
                elif cell == 2:
                    queue.append((i, j))
        
        # bfs on rotten oranges until queue is empty or all fresh have rotted
        while queue and fresh > 0:
            to_rot = len(queue)

            for _ in range(to_rot):
                i, j = queue.popleft()

                # rot nearby fresh
                # -- left
                if grid[i][max(j-1, 0)] == 1:
                    grid[i][j-1] = 2
                    fresh -= 1
                    queue.append((i, j-1))
                
                # -- up
                if grid[max(i-1, 0)][j] == 1:
                    grid[i-1][j] = 2
                    fresh -= 1
                    queue.append((i-1, j))
                
                # -- right
                if grid[i][min(j+1, m-1)] == 1:
                    grid[i][j+1] = 2
                    fresh -= 1
                    queue.append((i, j+1))
                
                # -- down
                if grid[min(i+1, n-1)][j] == 1:
                    grid[i+1][j] = 2
                    fresh -= 1
                    queue.append((i+1, j))
            
            # one more timestep finished
            answer += 1
        
        # if all fresh have rotted, return answer, else -1
        return answer if fresh == 0 else -1 
