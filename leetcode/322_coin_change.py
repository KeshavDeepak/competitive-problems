class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.dp = {}

        def f(idx, amount, coins_used):
            # base cases
            if amount == 0:
                return 0

            if idx == len(coins):
                return float('inf')
            
            # use memo if available
            if (idx, amount) in self.dp:
                return self.dp[(idx, amount)]

            # recursive cases
            if coins[idx] <= amount:
                min_coins = min(
                    f(idx, amount-coins[idx], coins_used+1) + 1, # take a coin and stay
                    f(idx+1, amount, coins_used) # dont take it and go next
                )

                # memoize
                self.dp[(idx, amount)] = min_coins

                return min_coins
            else: # can't take
                min_coins = f(idx+1, amount, coins_used) # go next

                # memoize
                self.dp[(idx, amount)] = min_coins

                return min_coins

        answer = f(0, amount, 0)

        return answer if answer != float('inf') else -1
