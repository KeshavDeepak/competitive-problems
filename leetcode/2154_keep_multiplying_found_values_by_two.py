import math

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        powers = []

        for num in nums:
            if num >= original and math.log(num/original, 2) % 1 == 0: # num is a power of original
                powers.append(num)
        
        # sort powers
        powers.sort()

        print(powers)

        # base cases
        if len(powers) == 0: return original

        if len(powers) == 1: 
            return original * 2 if powers[0] == original else original 

        # find biggest consecutive one
        for index in range(1, len(powers)):
            curr_value = powers[index]
            prev_value = powers[index-1]

            if curr_value == prev_value: continue

            if curr_value == prev_value * 2:
                continue
            else:
                return prev_value * 2
        
        # if th full array was parsed, biggest number is the answer
        return powers[-1] * 2
