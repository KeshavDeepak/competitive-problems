class Solution:
    def isSubsequence(self, s: str, t: str):
        s_pointer = 0
        t_pointer = 0
        
        while s_pointer < len(s) and t_pointer < len(t):
            if t[t_pointer] == s[s_pointer]:
                s_pointer += 1
            
            t_pointer += 1
        
        return True if s_pointer == len(s) else False

# main code
solution = Solution()

# test cases
print(solution.isSubsequence('abc', 'ahbfdc'))
print(solution.isSubsequence('axc', 'ahbfdc'))