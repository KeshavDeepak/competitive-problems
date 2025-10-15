class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        pre_cnt = 0
        cnt = 1
        k = 0
        
        for index in range(1, len(nums)):
            if nums[index] > nums[index - 1]:
                cnt += 1
            else:
                k = max(k, cnt // 2, min(pre_cnt, cnt))
                
                pre_cnt = cnt
                cnt = 1
        
        #* check once more 
        k = max(k, cnt // 2, min(pre_cnt, cnt))
        
        return k

#* main code
solution = Solution()

#* test cases
print(solution.maxIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1]))
print(solution.maxIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7]))
print(solution.maxIncreasingSubarrays([5,8,-2,-1]))