# top down
class Solution:
    def matrixMultiplication(self, arr):
        self.dp = {}
        
        def f(i, j):
            if i > j:
                return 0
                
            if i == j:
                return arr[i-1] * arr[i] * arr[i+1]
            
            if (i, j) in self.dp:
                return self.dp[(i, j)]
            
            answer = float('inf')
            
            for curr in range(i, j+1):
                left = f(i, curr-1)
                right = f(curr+1, j)
                
                answer = min(left + arr[i-1]*arr[curr]*arr[j+1] + right, answer)
            
            self.dp[(i, j)] = answer
            
            return answer
        
        
        return f(1, len(arr)-2)
