def generateParenthesis(n):
        def backtrack(string, open, close):
            # base case
            if len(string) == 2 * n:
                result.append(string)
                return
            
            # recursive case
            if open < n:
                backtrack(string + "(", open + 1, close)
            if close < open:
                backtrack(string + ")", open, close + 1)
            
        result = []
        backtrack("", 0, 0)
        return result
            
        

# print(generateParenthesis(1))
# print(generateParenthesis(2))
# print(generateParenthesis(3))
print(generateParenthesis(4))