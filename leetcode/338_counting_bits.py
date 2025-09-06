class Solution:
    def countBits(self, n: int):
        ans = []

        for i in range(n+1):
            ans.append(len([bit for bit in bin(i)[2:] if bit == "1"]))
        
        return ans


# main code
solution = Solution()

# test cases
print(solution.countBits(2))
print(solution.countBits(5))
