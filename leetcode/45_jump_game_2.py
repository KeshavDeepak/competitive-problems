class Solution:
    def jump(self, nums):
        dp_table = [0] * len(nums)
        
        for index in range(len(dp_table) - 2, -1, -1):
            if nums[index] == 0: 
                dp_table[index] = float('inf')
                continue
            
            dp_table[index] = min(dp_table[index+1:index+1+nums[index]]) + 1
        
        return dp_table[0]
        

# main code
solution = Solution()

# test cases
print(solution.jump([2,3,1,1,4]))
print(solution.jump([2,2,0,1,4]))