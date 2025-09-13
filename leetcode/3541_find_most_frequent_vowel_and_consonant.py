class Solution:
    def maxFreqSum(self, s: str):
        vowels = {'_' : 0}
        consonants = {'_' : 0}
        
        for letter in s:
            dictionary = vowels if letter in 'aeiou' else consonants 
            
            if letter in dictionary:
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1
        
        return max(vowels.values()) + max(consonants.values())
    
solution = Solution()

print(solution.maxFreqSum('successes'))
print(solution.maxFreqSum('aeiaeia'))
                