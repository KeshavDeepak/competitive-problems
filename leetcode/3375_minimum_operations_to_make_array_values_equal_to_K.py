def minOperations(nums, k: int) -> int:
        # sorted_unique_nums = sorted(set(nums)) # o(n log n) time complexity
        
        # # if any numbers are below k, then automatic fail
        # if sorted_unique_nums[0] < k:
        #     return -1
        
        # # delete k if it exists in the list
        # if k in sorted_unique_nums:
        #     sorted_unique_nums.remove(k)
        
        # # length of the list is the answer
        # return len(sorted_unique_nums)
        
        counter = 0
        nums = set(nums)
        
        for num in nums:
            # if any number is less than k, return -1
            if num < k:
                return -1
            
            # if number is more than k, increment counter
            if num > k:
                counter += 1
        
        return counter
            
        
        
            
            
            


# [5, 2, 5, 4, 5] -- [2, 4, 5] -- [4, 5]

print(minOperations([5, 2, 5, 4, 5], 2))
print(minOperations([2, 1, 2], 2))
print(minOperations([9,7,5,3], 1))