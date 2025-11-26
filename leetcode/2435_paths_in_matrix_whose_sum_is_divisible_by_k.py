class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[[0 for _ in range(k)] for _ in range(n)] for _ in range(m)]

        # base cases
        dp[0][0][grid[0][0] % k] = 1

        for j in range(1, n):
            rem = grid[0][j] % k

            for v in range(k):
                dp[0][j][v] = dp[0][j-1][v-rem]
        
        for i in range(1, m):
            rem = grid[i][0] % k

            for v in range(k):
                dp[i][0][v] = dp[i-1][0][v-rem]

        # recursive case
        for i in range(1, m):
            for j in range(1, n):
                prev_v = [x + y for (x, y) in zip(dp[i-1][j], dp[i][j-1])]
                rem = grid[i][j] % k

                for v in range(k):
                    dp[i][j][v] = prev_v[v-rem]
        
        # 
        return dp[-1][-1][0] % (10**9 + 7)

        
