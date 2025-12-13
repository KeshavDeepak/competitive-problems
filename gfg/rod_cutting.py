#User function Template for python3

class Solution:
    def cutRod(self, price):
        dp = [0] + price[:]
        
        for i in range(1, len(price)+1):
            l = 0
            r = i
            maxi = 0
            
            while l <= r:
                possible_sum = dp[l] + dp[r]
                
                if possible_sum > maxi: maxi = possible_sum
                
                l += 1
                r -= 1
            
            dp[i] = maxi
        
        return dp[-1]
