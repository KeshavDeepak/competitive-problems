class Solution:
    def canJump(self, nums):
        maxReach = 0
        
        for (index, num) in enumerate(nums):
            if index > maxReach: return False
            
            maxReach = max(maxReach, index+nums[index])
            
            if maxReach >= len(nums) - 1: return True
        


# main code
solution = Solution()

# test cases
print(solution.canJump([2,3,1,1,4]))

print(solution.canJump([3,2,1,0,4]))
