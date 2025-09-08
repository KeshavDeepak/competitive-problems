class Solution:
    def getNoZeroIntegers(self, n: int):
        for num in range(n, 0, -1):
            pairing_num = n - num
            
            if '0' not in str(num) + str(pairing_num):
                return [num, pairing_num]
        

# main code 
solution = Solution()

# test cases
print(solution.getNoZeroIntegers(2))
print(solution.getNoZeroIntegers(11))
print(solution.getNoZeroIntegers(21))