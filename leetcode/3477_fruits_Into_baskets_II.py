class Solution:
    def numOfUnplacedFruits(self, fruits, baskets) -> int:
        unplaced_fruits = 0
        
        baskets_used = [False] * len(baskets)
        
        for fruit in fruits:
            fruit_placed = False
            
            for (index, basket) in enumerate(baskets):
                if fruit <= basket and not baskets_used[index]:
                    # fruit has been placed
                    fruit_placed = True

                    # flag this basket in use
                    baskets_used[index] = True
                    
                    # exit the loop
                    break
            
            if not fruit_placed: 
                unplaced_fruits += 1
        
        return unplaced_fruits
                                 
    
    
# main
solution = Solution()

# test case 1
print(solution.numOfUnplacedFruits([4,2,5], [3,5,4]))

# test case 2
print(solution.numOfUnplacedFruits([3,6,1], [6,4,7]))