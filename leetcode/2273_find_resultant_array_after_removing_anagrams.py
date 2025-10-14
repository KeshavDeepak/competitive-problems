import copy

class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        #* base case
        if len(words) == 1: return words
        
        index = 0
        final_words = copy.deepcopy(words)
        
        while index < len(final_words) - 1:
            #* check if current element is an anagram of the element in front of it
            if ''.join(sorted(final_words[index])) == ''.join(sorted(final_words[index+1])):
                #* pop the element in front of current index
                final_words.pop(index + 1)
            else:
                #* move the index pointer to the next element
                index += 1
        
        return final_words


#* main code
solution = Solution()

#* test cases
print(solution.removeAnagrams(["abba","baba","bbaa","cd","cd"]))
print(solution.removeAnagrams(["a","b","c","d","e"]))
print(solution.removeAnagrams(["az", "azz"]))
