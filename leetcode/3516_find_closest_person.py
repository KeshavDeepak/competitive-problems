class Solution:
    def findClosest(self, x: int, y: int, z: int):
        x_diff = abs(z - x)
        y_diff = abs(z - y)
        
        if x_diff < y_diff:
            return 1
        elif x_diff > y_diff:
            return 2
        else:
            return 0

# main code
solution = Solution()

# test cases
print(solution.findClosest(2, 7, 4))
print(solution.findClosest(2, 5, 6))
print(solution.findClosest(1, 5, 3))