class Solution:
    def zeroFilledSubarray(self, nums) -> int:
        counter = 0
        num_of_subarrays = 0
        
        for num in nums+[1]: # a random element is added to the end of the input to ensure any final valid subarray is also accounted for 
            if num == 0: # we found a zero, increment counter
                counter += 1
            elif counter != 0: # we have reached a non-zero element and we were tracking a subarray
                num_of_subarrays += counter * (counter + 1) // 2
                
                # reset counter back to 0
                counter = 0
        
        return num_of_subarrays
        
        
#* main code
solution = Solution()

# test cases
print(solution.zeroFilledSubarray([1,3,0,0,2,0,0,4]))

print(solution.zeroFilledSubarray([0,0,0,2,0,0]))

print(solution.zeroFilledSubarray([2,10,2019]))
        

