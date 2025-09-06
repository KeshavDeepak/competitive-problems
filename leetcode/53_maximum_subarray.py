class Solution:
    def maxSubArray(self, nums):
        # initialize dp table
        dp_table = [0] * len(nums)
        
        # base case
        dp_table[0] = nums[0]
        
        # populate dp table
        for index in range(1, len(dp_table)):
            dp_table[index] = max(nums[index], dp_table[index - 1] + nums[index])
        
        # return maximum element in dp_table
        return max(dp_table)
        

# main code
solution = Solution()

# test cases
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(solution.maxSubArray([1]))
print(solution.maxSubArray([5,4,-1,7,8]))
