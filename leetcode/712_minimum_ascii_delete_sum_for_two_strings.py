# bottom up approach
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        s1 = ' ' + s1
        s2 = ' ' + s2

        m = len(s1)
        n = len(s2)

        # base case population
        # -- first row
        for j in range(1, n):
            dp[0][j] = ord(s2[j]) + dp[0][j-1]
        
        # -- first column
        for i in range(1, m):
            dp[i][0] = ord(s1[i]) + dp[i-1][0]
        
        # recursive case
        for i in range(1, m):
            for j in range(1, n):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        ord(s1[i]) + dp[i-1][j],
                        ord(s2[j]) + dp[i][j-1]
                    )
        
        #
        return dp[-1][-1]
    
# top down approach below
'''
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0 for _ in range(len(s2))] for _ in range(len(s1))]

        def f(i, j):
            # base cases
            if i == len(s1) and j == len(s2):
                return 0
            
            answer = 0
            
            if i == len(s1):
                for lett in s2[j:]:
                    answer += ord(lett)
                
                return answer
            
            if j == len(s2):
                for lett in s1[i:]:
                    answer += ord(lett)
                
                return answer
            
            if dp[i][j] != 0: # already computed in the past
                return dp[i][j]
            
            # recursive cases
            if s1[i] == s2[j]:
                answer = f(i+1, j+1)

                dp[i][j] = answer

                return answer
            
            # -- s1[i] != s2[j]
            answer = min(
                ord(s1[i]) + f(i+1, j),
                ord(s2[j]) + f(i, j+1)
            )

            dp[i][j] = answer

            return answer
        
        return f(0, 0)
'''