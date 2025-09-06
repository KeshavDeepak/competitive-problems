class Solution:
    def maxProfit(self, prices):
        min_price_seen = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            if price - min_price_seen > max_profit:
                max_profit = price - min_price_seen
            
            if price < min_price_seen:
                min_price_seen = price
        
        return max_profit

# main code
solution = Solution()

# test cases
print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.maxProfit([7,6,4,3,1]))
