def isValid(s: str) -> bool:
        pairs_of_brackets = {")" : "(", "]" : "[", "}" : "{"}
        
        stack = []
        
        for char in s:
            if char in pairs_of_brackets.values(): # open bracket
                stack.append(char)
            elif char in pairs_of_brackets.keys(): # close bracket
                if len(stack) == 0 or stack.pop() != pairs_of_brackets[char]:
                    return False # invalid string
        
        return len(stack) == 0


print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))