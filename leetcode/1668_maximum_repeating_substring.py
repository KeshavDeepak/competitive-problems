class Solution:
    def maxRepeating(self, sequence: str, word: str):
        if len(sequence) < len(word): return 0
        
        sequence = " " + sequence
        dp_array = [0] * len(sequence)
        
        m = len(word)

        for index in range(m, len(sequence)):
            if sequence[index-m+1:index+1] == word: dp_array[index] = dp_array[index-m] + 1
        
        return max(dp_array)
        

# main code
solution = Solution()

# test cases
print(solution.maxRepeating("ababc", "ab"))
print(solution.maxRepeating("abxabc", "ab"))
print(solution.maxRepeating("ababc", "ba"))
print(solution.maxRepeating("ababc", "ac"))
print(solution.maxRepeating("abcabc", "abc"))