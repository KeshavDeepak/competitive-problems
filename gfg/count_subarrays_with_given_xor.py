class Solution:
    def subarrayXor(self, arr, k):
        xors = {0:1}
        curr_xor = 0
        answer = 0
        
        for num in arr:
            curr_xor = curr_xor ^ num
            need = curr_xor ^ k
            
            if need in xors.keys():
                answer += xors[need]
        
            xors[curr_xor] = xors.get(curr_xor, 0) + 1
        
        return answer