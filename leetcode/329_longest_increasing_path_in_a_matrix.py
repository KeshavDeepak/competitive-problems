class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[-1] * n for _ in range(m)]

        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        self.ans = 1

        def dfs(i, j):
            if dp[i][j] != -1: return dp[i][j]

            # dfs on all sides if possible
            max_path = 0

            for dx, dy in directions:
                nx = i + dx
                ny = j + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue

                if matrix[i][j] >= matrix[nx][ny]:
                    continue
                max_path = max( max_path, dfs(nx, ny) )
            
            self.ans = max(self.ans, max_path + 1)
            dp[i][j] = max_path + 1

            return max_path + 1
        
        for i in range(m):
            for j in range(n):
                dfs(i, j)

        return self.ans


        
