class Solution:
    def largestPerimeter(self, nums):
        nums.sort(reverse=True)
        
        for index in range(2, len(nums)):
            if nums[index] + nums[index - 1] > nums[index - 2]: # found a solution
                return nums[index] + nums[index - 1] + nums[index - 2]
        
        return 0
        

# main code
solution = Solution()

# test cases
print(solution.largestPerimeter([2, 1, 2]))
print(solution.largestPerimeter([1, 2, 1, 10]))
