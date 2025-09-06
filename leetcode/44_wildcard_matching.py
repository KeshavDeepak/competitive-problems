from pprint import pprint

class Solution:
    def isMatch(self, s: str, p: str):
        s = ' ' + s
        p = ' ' + p
        
        # initialize dp_table
        dp_table = [[False for x in range(len(s))] for y in range(len(p))]
        
        # base case population
        dp_table[0][0] = True # empty string always matches an empty pattern
        
        for row_index in range(1, len((dp_table))): # an empty string might match a * if it is at the start
            if p[row_index] == "*":
                dp_table[row_index][0] = dp_table[row_index - 1][0]
        
        # populate the rest of the dp_table
        for row in range(1, len(dp_table)):
            for column in range(1, len(dp_table[0])):
                if p[row] == "*":
                    dp_table[row][column] = dp_table[row][column-1] or \
                                            dp_table[row-1][column-1] or \
                                            dp_table[row-1][column]
                elif p[row] == s[column] or p[row] == "?":
                    dp_table[row][column] = dp_table[row-1][column-1]
        
        # return bottom-right element of dp_table
        return dp_table[-1][-1]
        

# main code
solution = Solution()

# test cases
# print(solution.isMatch("aa", "a"))
# print(solution.isMatch("aa", "*"))
# print(solution.isMatch("cb", "?a"))
# print(solution.isMatch("adceb", "*a?b"))
# print(solution.isMatch("bca", "bc*"))
print(solution.isMatch("adceb", "*a*b"))