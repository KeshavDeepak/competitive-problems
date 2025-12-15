class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        self.dp = {}

        def f(idx, t, buy):
            # base cases
            if idx == len(prices) or t == 0: 
                return 0

            # if already memoized, use it
            if (idx, t, buy) in self.dp:
                return self.dp[(idx, t, buy)]
            
            # recursive case
            if buy:
                profit = max(
                    -prices[idx] + f(idx+1, t, False), # buy
                    f(idx+1, t, True) # no buy
                )

                # memoize
                self.dp[(idx, t, buy)] = profit

                #
                return profit
            else:
                profit = max(
                    prices[idx] + f(idx+1, t-1, True), # sell
                    f(idx+1, t, False) # no sell
                )

                # memoize
                self.dp[(idx, t, buy)] = profit
                
                #
                return profit
        
        return f(0, k, True)
        
