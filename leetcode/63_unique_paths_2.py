class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        # base case
        if obstacleGrid[0][0] == 1: 
            return 0 # cannot start at starting position because rock is there
        else:
            obstacleGrid[0][0] = 1
        
        # populate first row
        for index in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][index] == 1: # rock found
                obstacleGrid[0][index] = 0
                continue
            
            obstacleGrid[0][index] = obstacleGrid[0][index-1]
        
        # populate first column
        for index in range(1, len(obstacleGrid)):
            if obstacleGrid[index][0] == 1: # rock found
                obstacleGrid[index][0] = 0
                continue
            
            obstacleGrid[index][0] = obstacleGrid[index - 1][0]
        
        # populate the rest of the table
        for row in range(1, len(obstacleGrid)):
            for column in range(1, len(obstacleGrid[0])):
                if obstacleGrid[row][column] == 1: # rock found
                    obstacleGrid[row][column] = 0
                    continue
                
                obstacleGrid[row][column] = obstacleGrid[row][column-1] + obstacleGrid[row-1][column]
        
        # return bottom-right element of table
        return obstacleGrid[-1][-1]

# main code
solution = Solution()

# test cases
print(solution.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
print(solution.uniquePathsWithObstacles([[0,1],[0,0]]))
print(solution.uniquePathsWithObstacles([[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0]]))
print(solution.uniquePathsWithObstacles([[0,0],[1,1],[0,0]]))

        