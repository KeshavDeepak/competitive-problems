class Solution:
    def maximumEnergy(self, energy: list[int], k: int) -> int:
        dp_table = energy[:k] + [0] * (len(energy)-k)
        
        for index in range(k, len(dp_table)):
            dp_table[index] = max(energy[index],
                                  dp_table[index-k] + energy[index] 
            )
            
            # print(energy[index], " : ", [energy[index], dp_table[index-k] + energy[index], *dp_table[index-k+1:index]])
        
        # print(dp_table)
        return max(dp_table[-k:])


#* main code
solution = Solution()

#* test cases
print(solution.maximumEnergy([5,2,-10,-5,1], 3)) # 3

print(solution.maximumEnergy([-2,-3,-1], 2)) # -1

print(solution.maximumEnergy([5,-10,4,3,5,-9,9,-7], 2)) # 23

print(solution.maximumEnergy([-1,3,-4,-7], 2)) # -4



