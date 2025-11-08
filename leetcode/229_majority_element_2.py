class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        answer = []
        threshold = len(nums) // 3

        # find potential candidates
        candidate_1, candidate_2 = None, None
        counter_1, counter_2 = 0, 0

        for num in nums:
            if num == candidate_1:
                counter_1 += 1
            elif num == candidate_2:
                counter_2 += 1
            elif counter_1 == 0:
                candidate_1 = num
                counter_1 += 1
            elif counter_2 == 0:
                candidate_2 = num
                counter_2 += 1
            else:
                counter_1 -= 1
                counter_2 -= 1
        
        # verify both potential candidates
        freq_1 = 0
        freq_2 = 0
        
        for num in nums:
            if num == candidate_1:
                freq_1 += 1
            elif num == candidate_2:
                freq_2 += 1
        
        if freq_1 > threshold:
            answer.append(candidate_1)
        
        if freq_2 > threshold:
            answer.append(candidate_2)
        
        # 
        return answer
        
        
