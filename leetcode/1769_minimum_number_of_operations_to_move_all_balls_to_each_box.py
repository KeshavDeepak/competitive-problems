class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        prefix_sum = [0] * len(boxes)
        suffix_sum = [0] * len(boxes)
        
        #* populate prefix sum
        counter = 0 if boxes[0] == '0' else 1
        
        for index in range(1, len(boxes)):
            prefix_sum[index] = prefix_sum[index-1] + counter
            
            if boxes[index] == '1': counter += 1
        
        #* populate suffix sum
        counter = 0 if boxes[-1] == '0' else 1
        
        for index in range(len(boxes)-2, -1, -1):
            suffix_sum[index] = suffix_sum[index+1] + counter
            
            if boxes[index] == '1': counter += 1
        
        #* add both sum arrays to get final answer and return it
        return [x+y for x, y in zip(prefix_sum, suffix_sum)]



#* main code
solution = Solution()

#* test cases
print(solution.minOperations('110'))
print(solution.minOperations('001011'))