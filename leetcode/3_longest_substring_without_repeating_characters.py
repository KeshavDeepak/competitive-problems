def lengthOfLongestSubstring(s) -> int:
        char_to_index = {}
        current_substring = ""
        longest_substring_length = 0
        
        for index, char in enumerate(s):
            if char in current_substring: # char is in current_substring
                # update longest_substring if a new longest substring has been found
                longest_substring_length = max(longest_substring_length, len(current_substring))
                
                # update current_substring to previous occurrence of char plus one ahead
                current_substring = s[char_to_index[char]+1:index+1]

            else: # char is not in current_substring
                current_substring += char
                
            # add/update char in char_to_index
            char_to_index[char] = index
            
            # print(char, current_substring, longest_substring)
    
        # do a final check of current_substring to update longest_substring in case the last substring in s is the longest
        longest_substring_length = max(longest_substring_length, len(current_substring))
        
        return longest_substring_length


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring(" "))
            