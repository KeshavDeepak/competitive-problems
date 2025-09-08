class Solution:
    def sumZero(self, n: int):
        nums = []
        
        for i in range(-(n//2), n//2+1):
            if i == 0 and n % 2 == 0:
                continue
            
            nums.append(i)

        return nums    
    
        
# main code
solution = Solution()

# test cases
print(solution.sumZero(5))
print(solution.sumZero(3))
print(solution.sumZero(4))
print(solution.sumZero(1))
        