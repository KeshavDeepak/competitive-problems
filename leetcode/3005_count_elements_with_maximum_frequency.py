class Solution:
    def maxFrequencyElements(self, nums):
        num_to_freq = {}
        
        for num in nums:
            if num in num_to_freq:
                num_to_freq[num] += 1
            else:
                num_to_freq[num] = 1
        
        max_freq = max(num_to_freq.values())
        counter = 0
        
        for num in num_to_freq:
            if num_to_freq[num] == max_freq:
                counter += 1
        
        return max_freq * counter


# main code
solution = Solution()

# test cases
print(solution.maxFrequencyElements([1, 2, 2, 3, 1, 4]))
print(solution.maxFrequencyElements([1, 2, 3, 4, 5]))