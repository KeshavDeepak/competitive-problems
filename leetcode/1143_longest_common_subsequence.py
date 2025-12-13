class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # initialize dp
        dp = [[0] * (len(text1)+1) for _ in range(len(text2)+1)]

        # populate dp
        for i in range(1, len(text2)+1):
            for j in range(1, len(text1)+1):
                chr1 = text1[j-1]
                chr2 = text2[i-1]
                
                if chr1 == chr2:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(
                        dp[i][j-1],
                        dp[i-1][j],
                        # dp[i-1][j-1] is not needed because it cannot exceed the other two above
                    )
        #
        return dp[-1][-1]
