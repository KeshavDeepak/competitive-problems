class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0

        while i <= len(bits)-2:
            if bits[i] == 1: 
                if i == len(bits) - 2: # not valid, it is using the last 0
                    return False
                
                i += 2
            else:
                i += 1
        
        return True
