def longestCommonPrefix(strs) -> str:
        # handle edge cases with empty strings
        if "" in strs:
            return ""
        
        # main cases
        prefix = strs[0]
        
        for string in strs[1:]:
            index = 0
            
            for index, char in enumerate(string):
                # if string is longer than the prefix
                if index >= len(prefix):
                    break
                
                # if the characters do not match
                if prefix[index] != char:
                    prefix = string[:index]
                    break
                
            # if string is shorter than the prefix
            if index < len(prefix):
                prefix = prefix[:index+1]
        
        return prefix
                
# print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["ab", "a"]))
# print(longestCommonPrefix(["", ""]))
# print(longestCommonPrefix(["abab","aba",""]))
# print(longestCommonPrefix(["flow", "flower"]))
        
        