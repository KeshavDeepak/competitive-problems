class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        # add padding column and row
        for row_index in range(len(matrix)):
            matrix[row_index] = ['0'] + matrix[row_index]
        
        matrix.insert(0, ['0'] * len(matrix[0]))

        # dp table
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        # maximal square
        maximal_square = 0

        # main code
        for row_index in range(1, len(matrix)):
            for col_index in range(1, len(matrix[0])):
                if matrix[row_index][col_index] == '0': continue

                dp[row_index][col_index] = min(
                    dp[row_index-1][col_index], dp[row_index-1][col_index-1], dp[row_index][col_index-1]
                ) + 1

                if dp[row_index][col_index] ** 2 > maximal_square: 
                    maximal_square = dp[row_index][col_index] ** 2
        
        return maximal_square

        