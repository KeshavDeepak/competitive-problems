class Solution:
    def uniquePaths(self, m: int, n: int):
        # initialize the dp_table
        dp_table = [[0] * n] * m
        
        # base case
        dp_table[0] = [1] * n
        dp_table = [[1] + row[1:] for row in dp_table]
        
        # populate the rest of the dp_table
        for row in range(1, m):
            for column in range(1, n):
                dp_table[row][column] = dp_table[row][column-1] + dp_table[row-1][column]
        
        # return the bottom-right element of the dp_table
        return dp_table[-1][-1]
        
        
    
# main code
solution = Solution()

# test cases
print(solution.uniquePaths(3, 7))
print(solution.uniquePaths(3, 2))
print(solution.uniquePaths(5, 5))