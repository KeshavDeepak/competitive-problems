class Solution:
    def minTime(self, skill: list[int], mana: list[int]) -> int:
        dp_table = [0] * (len(skill) + 1)
        
        skill = [0] + skill
        
        for potion in mana:
            #* forward pass
            for wizard_index in range(1, len(dp_table)):
                dp_table[wizard_index] = max(dp_table[wizard_index], dp_table[wizard_index - 1]) + \
                                            skill[wizard_index] * potion
            
            #* backward pass
            for wizard_index in range(len(dp_table)-2, -1, -1):
                dp_table[wizard_index] = dp_table[wizard_index + 1] - \
                                            skill[wizard_index + 1] * potion
        
        return dp_table[-1]


# main code
solution = Solution()

# test cases
print(solution.minTime([1, 5, 2, 4], [5, 1, 4, 2]))
print(solution.minTime([1, 1, 1], [1, 1, 1]))