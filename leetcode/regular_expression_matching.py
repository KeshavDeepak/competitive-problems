from tabulate import tabulate

def isMatch(s: str, p: str) -> bool:
        dp_table = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # empty pattern always matches empty string
        dp_table[0][0] = True      
        
        # check for * in the first row and deal with them appropriately
        for index in range(1, len(dp_table[0])):
            pattern_index = index - 1
            
            if p[pattern_index] == "*":
                dp_table[0][index] = dp_table[0][index - 2]
        
        # populate the rest of the dp table
        for row_index in range(1, len(dp_table)):
            row = dp_table[row_index]
            
            for column_index in range(1, len(row)):

                current_pattern_char = p[column_index - 1]
                current_string_char = s[row_index - 1]
                
                if current_pattern_char == current_string_char or current_pattern_char == ".":
                    dp_table[row_index][column_index] = dp_table[row_index - 1][column_index - 1]
                elif current_pattern_char == "*":
                    if p[column_index - 2] == current_string_char or p[column_index - 2] == ".":
                        dp_table[row_index][column_index] = dp_table[row_index][column_index - 2] \
                                                            or dp_table[row_index - 1][column_index - 1] \
                                                            or dp_table[row_index - 1][column_index]
                    else: # previous char does not match current_string_char
                        dp_table[row_index][column_index] = dp_table[row_index][column_index - 2]
                        
        print(tabulate(dp_table, headers=["_"] + list(p), showindex=["_"] + list(s), tablefmt="fancy_grid"))
        print(dp_table[len(dp_table) - 1][len(dp_table[0]) - 1])
        
        return dp_table[len(dp_table) - 1][len(dp_table[0]) - 1]
        
# isMatch("aa", "a*")   
# isMatch("aa", "a")
# isMatch("aabb", "a*b.c")
isMatch("aaa", "ab*a*c*a")
# isMatch("aaa", ".*")
# isMatch("a", "..*")

                