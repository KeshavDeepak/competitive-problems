class Solution:
    def numDecodings(self, s):
        # if leading zero exists, return 0 by default
        if s[0] == '0': return 0
        
        # initialize dp_table 
        dp_table = [0] * (len(s) + 1)
        
        # base case
        dp_table[0] = 1
        dp_table[1] = 1
        
        # populate the dp_table by moving across s
        s = ' ' + s
        
        for index in range(2, len(s)):
            # can the current digit act on its own, if so, add previous element
            if s[index] != '0': dp_table[index] += dp_table[index-1]
            
            # can the current digit act with the previous digit as a pair, if so, add the previous-to-previous element
            if s[index-1] != '0' and 0 <= int(s[index-1] + s[index]) <= 26: dp_table[index] += dp_table[index-2]
                
        return dp_table[-1]

# main code
solution = Solution()

# test cases
print(solution.numDecodings("12"))
print(solution.numDecodings("226"))
print(solution.numDecodings("06"))
print(solution.numDecodings("11106"))