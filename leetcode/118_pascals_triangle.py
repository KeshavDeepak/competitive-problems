class Solution:
    def generate(self, numRows: int):
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1, 1]]
                
        dp_table = [[1],[1,1]]
        
        for _ in range(numRows-2):
            temp = []
            
            for index in range(1, len(dp_table[-1])):
                temp.append(dp_table[-1][index] + dp_table[-1][index-1])
            
            dp_table.append([1, *temp, 1])

        return dp_table

# main code
solution = Solution()

# test cases
print(solution.generate(5))
print(solution.generate(4))
print(solution.generate(3))
print(solution.generate(1))
        