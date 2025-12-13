class Solution:
    def isSubsetSum (self, arr, sum):
        dp = set()
        
        for num in arr:
            new_elems = set()
            
            # process num 
            if num == sum:
                return True
            elif num < sum:
                new_elems.add(num)
            else:
                continue
            
            # iterate through dp and build on top if possible
            for val in dp:
                new_sum = num + val
                
                if new_sum == sum:
                    return True
                elif new_sum < sum:
                    # add to dp
                    new_elems.add(new_sum)
            
            # update dp 
            dp.update(new_elems)
        
        # if reached here, no valid subset was found
        return False
