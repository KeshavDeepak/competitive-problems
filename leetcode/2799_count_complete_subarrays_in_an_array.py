class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        left = 0
        right = 0
        subarray = {}
        n = len(nums)
        total_distinct_elements = len(set(nums))
        output_count = 0

        while right != len(nums) and left != len(nums):
            # increment current element's frequency
            subarray[nums[right]] = subarray.get(nums[right], 0) + 1

            # check if subarray has correct number of distinct elements
            while len(subarray.keys()) == total_distinct_elements: 
                # if it does than add current subarray plus all possible additions from the right-hand side to output_count
                output_count += n - right 
            
                # decrement frequency of element at the left pointer
                subarray[nums[left]] -= 1
                if subarray[nums[left]] == 0: del subarray[nums[left]]

                # move left pointer one step to the right if lesser than right pointer
                left += 1
            
            right += 1
        
        return output_count
    
#* main code
solution = Solution()

#* test cases
print(solution.countCompleteSubarrays([1, 3, 1, 2, 2]))
print(solution.countCompleteSubarrays([5, 5, 5, 5]))