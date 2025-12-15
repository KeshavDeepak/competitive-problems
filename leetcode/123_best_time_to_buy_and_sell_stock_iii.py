class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.dp = {}

        def f(idx, transactions_left, canBuy):
            # base case
            if transactions_left == 0 or idx == len(prices):
                return 0
            
            # if memoized already, use it
            if (idx, transactions_left, canBuy) in self.dp:
                return self.dp[(idx, transactions_left, canBuy)]
            
            # recursive case
            if canBuy:
                # buy
                profit_buy = -prices[idx] + f(idx+1, transactions_left, False)

                # dont buy
                profit_no_buy = f(idx+1, transactions_left, True)

                # calculate max profit
                profit = max(profit_buy, profit_no_buy)

                # memoize
                self.dp[(idx, transactions_left, canBuy)] = profit

                #
                return profit
            else:
                # sell
                profit_sell = prices[idx] + f(idx+1, transactions_left-1, True)

                # dont sell
                profit_no_sell = f(idx+1, transactions_left, False)

                # calculate max profit
                profit = max(profit_sell, profit_no_sell)

                # memoize
                self.dp[(idx, transactions_left, canBuy)] = profit

                #
                return profit

        
        return f(0, 2, True)
