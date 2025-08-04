def longestValidParentheses(s: str) -> int:
        stack = []
        one_hot_encoding = [False] * len(s)
        
        for index, char in enumerate(s):
            if char == "(":
                stack.append(index)
            else: # char is ")"
                if stack and s[stack[-1]] == "(":
                    one_hot_encoding[index] = True
                    one_hot_encoding[stack[-1]] = True
                    
                    stack.pop()
        
        # find biggest substring of Trues in one_hot_encoding
        longest = 0
        current = 0
        
        for value in one_hot_encoding:
            if value:
                current += 1
            else:
                longest = max(longest, current)
                current = 0
                
        longest = max(longest, current)
        
        return longest

def longestValidParentheses(s: str) -> int:
        dp_table = [0] * (len(s) + 1)
        
        for string_index, bracket in enumerate(s):
            dp_table_index = string_index + 1
            if bracket == ")":
                if string_index > 0: # at least one preceding character exists
                    if s[string_index - 1] == "(":
                        dp_table[dp_table_index] = dp_table[dp_table_index - 2] + 2
                    else: # s[index - 1] is ")"
                        if (string_index - dp_table[dp_table_index - 1] - 1) >= 0 and s[string_index - dp_table[dp_table_index - 1] - 1] == "(":
                        # if s[string_index - dp_table[dp_table_index - 1] - 1] == "(":
                            dp_table[dp_table_index] = 2 + dp_table[dp_table_index - 1] + dp_table[dp_table_index - dp_table[dp_table_index - 1] - 2] 
        
        # print(dp_table)
        return max(dp_table)
                
        


# print(longestValidParentheses("(()"))
# print(longestValidParentheses(")()()(()"))
# print(longestValidParentheses(")()())("))
# print(longestValidParentheses("()(())"))
print(longestValidParentheses("(()))())("))
                
                    