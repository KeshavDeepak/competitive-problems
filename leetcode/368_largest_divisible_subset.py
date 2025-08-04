def largestDivisibleSubset(nums):
        # sort the list
        nums.sort()
        
        # dp_array - each element is a tuple - (number, [longest divisible subset where this number is the biggest number])
        dp = []
        
        for current_num in nums:
            # find the best divisible number (one that has the biggest subset) that already exists in dp
            current_best_divisible_subset = []
            
            for potential_num, potential_subset in dp:
                if current_num % potential_num == 0 and len(potential_subset) > len(current_best_divisible_subset):
                    current_best_divisible_subset = potential_subset.copy()
            
            # add the current number to the best divisible subset
            current_best_divisible_subset.append(current_num)
            
            # add the best divisible subset to dp
            dp.append((current_num, current_best_divisible_subset))

        return max(dp, key=lambda x: len(x[1]))[1]


print(largestDivisibleSubset([1,2,4,8]))
print(largestDivisibleSubset([1,2,3]))
            
                    