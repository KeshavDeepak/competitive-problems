class Solution:
    def totalFruit(self, fruits):
        # fruit_type : latest_index_position
        fruits_picked = {}
        
        # fruit pickings possible
        fruit_pickings_nums = []
        
        # pointer depicting start of current fruit picking session 
        start_pointer = 0
        
        for index, fruit in enumerate(fruits):
            # if two fruits have not yet been chosen, then add/update current fruit without any further checks
            if len(fruits_picked) < 2:
                fruits_picked[fruit] = index
                continue
            
            # if two fruits have already been picked
            if fruit not in fruits_picked.keys(): # reached the end of current picking session
                # add current fruit picking session to history
                fruit_pickings_nums.append(1 + (index - 1) - start_pointer)
                
                # find the fruit that appears earlier in the session
                earlier_fruit = min(fruits_picked, key=fruits_picked.get)
                
                # update start pointer to one more than the earlier fruit's index
                start_pointer = fruits_picked[earlier_fruit] + 1
                
                # remove the earlier fruit from the dictionary
                del fruits_picked[earlier_fruit]
                
                # add the new fruit to the dictionary
                fruits_picked[fruit] = index
            
            else: # fruit exists, update latest index value
                fruits_picked[fruit] = index
        
        # add the last fruit picking session to history
        fruit_pickings_nums.append(len(fruits) - start_pointer)
        
        # return the maxmimum value of fruit_pickings_num
        return max(fruit_pickings_nums)

# main 
solution = Solution()

# test case 1
print(solution.totalFruit([1, 2, 3, 2, 2]))

# test case 2
print(solution.totalFruit([0, 1, 2, 2]))

# test case 3
print(solution.totalFruit([1, 2, 1]))