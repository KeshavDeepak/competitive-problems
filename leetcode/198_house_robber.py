class Solution:
    def rob(self, nums):
        dp_table = [0, nums[0]]
        nums = [0] + nums
         
        for i in range(2, len(nums)):
            dp_table.append(max(dp_table[i-1],nums[i]+dp_table[i-2]))
        
        return dp_table[-1]
             
        

# main code
solution = Solution()

# test cases
print(solution.rob([1, 2, 3, 1]))
print(solution.rob([2, 7, 9, 3, 1]))
        

'''
1 --> What is the dp table?
[1, 2, 4, 4]

2 --> base case population
[0, 1, _, _, _]
[0, 1, 2, 4, 1]

3 --> how to populate the rest? -- recurrence relation : dp[i] = max(dp[i-2]+dp[i],dp[i-1]) -- why?
[0, 1, 2, 4, 4]

4 --> where is the final answer?
at the end


one more dry run (2, 7, 9, 3, 1) :
[0, 2, 7, 11, 11, 12]
'''