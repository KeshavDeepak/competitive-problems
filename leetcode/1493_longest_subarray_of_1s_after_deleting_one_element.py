class Solution:
    def longestSubarray(self, nums):
        left = 0
        right = 0
        pos_of_zero = -1
        longest_subarray_length = 0
        
        while right != len(nums):
            if nums[right] == 0:
                if pos_of_zero == -1: # we can tolerate one zero so its fine
                    pos_of_zero = right
                else: # we have encountered another zero, update longest_subarray_length, left pointer and pos_of_zero
                    longest_subarray_length = max(longest_subarray_length, right-left-1)
                    left = pos_of_zero + 1
                    pos_of_zero = right
            
            right += 1
        
        # handle case where there is an unchecked subarray at the end of nums
        longest_subarray_length = max(longest_subarray_length, right-left-1)
        
        return longest_subarray_length

            
            

# main code
solution = Solution()

# test cases
print(solution.longestSubarray([1,1,0,1]))

print(solution.longestSubarray([0,0,0,0]))

print(solution.longestSubarray([0,1,1,1,0,1,1,0,1]))

print(solution.longestSubarray([1,1,1]))

print(solution.longestSubarray([]))