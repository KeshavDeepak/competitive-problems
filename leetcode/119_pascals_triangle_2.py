class Solution:
    def getRow(self, rowIndex: int):
        # initialize dp_table
        dp_table = [
            [1],
            [1, 1]
        ]
        
        # base case
        if rowIndex == 0 or rowIndex == 1:
            return dp_table[rowIndex]

        # populate dp_table
        for _ in range(2, rowIndex + 1):
            new_row = [dp_table[-1][index] + dp_table[-1][index+1] for index in range(len(dp_table[-1]) - 1)]
            
            # append new row to dp_table
            dp_table.append([1] + new_row + [1])
        
        # return last element of dp_table
        return dp_table[-1]

# main code
solution = Solution()

# test cases
print(solution.getRow(3))
print(solution.getRow(0))
print(solution.getRow(1))
        