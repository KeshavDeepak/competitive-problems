class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        #* princess' cell is the base case
        dungeon[-1][-1] = max(1 + dungeon[-1][-1] * -1, 1)
        
        #* populate the last row
        for column_index in range(len(dungeon[0])-2, -1, -1):
            dungeon[-1][column_index] = max(dungeon[-1][column_index] * -1 + dungeon[-1][column_index+1], 1)
            
        #* populate the last column
        for row_index in range(len(dungeon)-2, -1, -1):
            dungeon[row_index][-1] = max(dungeon[row_index][-1] * -1 + dungeon[row_index + 1][-1], 1)
        
        # print("\n".join([str(row) for row in dungeon]))
        
        #* populate the rest of the table
        for row_index in range(len(dungeon)-2, -1, -1):
            for column_index in range(len(dungeon[0])-2, -1, -1):
                dungeon[row_index][column_index] = \
                    max(min(dungeon[row_index + 1][column_index], dungeon[row_index][column_index + 1]) + \
                        dungeon[row_index][column_index] * -1,
                        
                        1)
        
        return dungeon[0][0]
                
        
# main code 
solution = Solution()

# test cases
print(solution.calculateMinimumHP([
    [-2,-3,3],
    [-5,-10,1],
    [10,30,-5]
]))