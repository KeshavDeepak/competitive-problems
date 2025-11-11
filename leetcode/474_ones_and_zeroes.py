class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {
            (0, 0) : 0
        }

        for string in strs:
            str_zeros = 0
            str_ones = 0

            for char in string:
                if char == '0':
                    str_zeros += 1
                else: # char = 1
                    str_ones += 1
            
            new_dp = dp.copy()
            
            for combo in dp:
                combo_added = (combo[0] + str_zeros, combo[1] + str_ones)
                
                if combo_added[0] <= m and combo_added[1] <= n:
                    if combo_added not in dp:
                        new_dp[combo_added] = dp[combo] + 1
                    elif dp[combo_added] < dp[combo] + 1:
                        new_dp[combo_added] = dp[combo] + 1
            
            dp = new_dp

        # answer is maximal value among dp's values
        print(dp)
        return max(dp.values())


