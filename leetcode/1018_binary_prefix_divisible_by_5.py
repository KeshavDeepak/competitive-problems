class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        value = 0
        answer = []

        for num in nums:
            value = value*2 + num

            answer.append(True if value % 5 == 0 else False)
        
        return answer

