class Solution:
    def equalFrequency(self, word: str) -> bool:
        d = {}
        
        for char in word:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
                
        


'''
ddaccbb

a  b  c  d  
[1, 1, 2, 2] -- 1
[0, 0, 1, 1] -- false

abcc

a   b  c
[1, 1, 2]  -- 1
[0, 0, 1] -- true

abc

 a  b  c
[1, 1, 1] -- 1
[0, 0, 0] -- true


'''     

#!! not solved
        
        
        
                    
                
                


        



        