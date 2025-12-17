from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        queue = deque([])
        answer = [[0] * m for _ in range(n)]
        visited = set()

        # add all 0s to queue
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i, j))
        
        # multi-source bfs
        layer = 0

        while queue:
            length = len(queue)

            for _ in range(length):
                i, j = queue.popleft()
                if (i, j) in visited:
                    continue
                
                visited.add((i, j))
                answer[i][j] = layer

                # add all neighbors to queue
                if j != 0:
                    queue.append((i, j-1))
                
                if i != 0:
                    queue.append((i-1, j))
                
                if j != m-1:
                    queue.append((i, j + 1))
                
                if i != n-1:
                    queue.append((i+1, j))
                
            layer += 1
        
        return answer
