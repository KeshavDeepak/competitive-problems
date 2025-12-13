#User function Template for python3

class Solution:
    def maximumPoints(self, arr):
        # Code here
        dp = arr[0]
        
        for i in range(1, len(arr)):
            new_dp = [0, 0, 0]
            
            new_dp[0] = arr[i][0] + max(dp[1], dp[2])
            new_dp[1] = arr[i][1] + max(dp[0], dp[2])
            new_dp[2] = arr[i][2] + max(dp[0], dp[1])
            
            dp = new_dp
        
        # 
        return max(dp)
