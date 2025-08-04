from tabulate import tabulate

def longestPalindrome(s: str) -> str:
        # dp[i][j] is True if s[i:j] is a palindrome
        dp = [[False] * len(s) for _ in range(len(s))]
        
        # current longest palindrome found
        longest_palindrome = "" if not s else s[0]
        
        # fill in the table for length 1 substrings
        for i in range(len(dp)):
            dp[i][i] = True
        
        # if s doesnt have more than one char, exit
        # if len(s) <= 1:
        #     return longest_palindrome
        
        # fill in the table for length 2 substrings manually
        for i in range(len(dp) - 1):
            if s[i] == s[i+1]:
                # update the dp table
                dp[i][i+1] = True
                
                # check for a new longest palindrome
                if len(longest_palindrome) < 2:
                    longest_palindrome = s[i:i+2] 
        
        # if s doesnt have more than 2 characters, exit 
        # if len(s) <= 2:
        #     return longest_palindrome
        
        # fill in the rest of the table in a diagonal fashion (going one substring length at a time) except the top-right-most square
        for i in range(len(dp) - 2):
            for row in range(0, len(dp) - 2 - i):
                # calculate column from row
                column = row + 2 + i 
                
                # print(row, column, s[row], s[column])
                
                # if current two characters are equal and the characters inside them (row+1,column-1) are also a palindrome -- then it is also a palindrome
                if s[row] == s[column] and dp[row + 1][column - 1]:
                    dp[row][column] = True
                    
                    # check for new longest palindrome
                    if len(longest_palindrome) < (1 + column - row):
                        longest_palindrome = s[row:column+1]
        
        # print(tabulate(dp, headers=list(s), showindex=list(s), tablefmt="fancy_grid"))
        return longest_palindrome

print(longestPalindrome("babad"))
print(longestPalindrome("dbbd"))
print(longestPalindrome("bb"))
print(longestPalindrome(""))
print(longestPalindrome("a"))