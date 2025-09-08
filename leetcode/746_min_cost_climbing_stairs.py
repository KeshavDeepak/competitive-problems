class Solution:
    def minCostClimbingStairs(self, cost):
        dp_table = [0, 0]
        
        for i in range(2, len(cost) + 1):
            dp_table.append(min(cost[i-2]+dp_table[i-2],cost[i-1]+dp_table[i-1]))
            
        return dp_table[-1]


# main code
solution = Solution()

# test cases
print(solution.minCostClimbingStairs([10,15,20]))
print(solution.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
        
    