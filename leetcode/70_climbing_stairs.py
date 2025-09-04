class Solution:
    def climbStairs(self, n: int):
        # base cases
        if n == 1 or n == 0: return 1
        if n == 2: return 2
        
        # dp table
        dp_table = [0] * n
        
        # dp table base case
        dp_table[0] = 1
        dp_table[1] = 2
        
        # populate dp table
        for index in range(2, len(dp_table)):
            dp_table[index] = dp_table[index - 1] + dp_table[index - 2]
        
        # return last element
        return dp_table[-1]
        

# main code
solution = Solution()

# test cases
print(solution.climbStairs(2))
print(solution.climbStairs(3))
print(solution.climbStairs(5))
print(solution.climbStairs(6))
