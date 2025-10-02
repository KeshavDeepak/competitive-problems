class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        #* base case
        if len(prices) == 1: return 0
        
        total_max_profit = 0

        #* add net profits between consecutive days
        for index in range(1, len(prices)):
            total_max_profit += max(0, prices[index] - prices[index-1])
        
        return total_max_profit
        
        
        

# main code 
solution = Solution()

# test cases
print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.maxProfit([1,2,3,4,5]))
print(solution.maxProfit([7,6,4,3,1]))