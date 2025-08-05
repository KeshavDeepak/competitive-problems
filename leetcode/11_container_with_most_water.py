class Solution:
    def maxArea(self, height) -> int:
        left_pointer = 0
        right_pointer = len(height) - 1
        
        max_area = 0
        
        while left_pointer < right_pointer:
            left_water_level = height[left_pointer]
            right_water_level = height[right_pointer]
            
            # calculate area between left and right pointers
            area = min(left_water_level, right_water_level) * (right_pointer - left_pointer)
            
            # update max_area to area if area is greater
            if area > max_area: max_area = area
            
            # move the pointer pointing to the lower water level
            if left_water_level < right_water_level:
                left_pointer += 1
            else:
                right_pointer -= 1
        
        return max_area


# main code
solution = Solution()


# test case 1
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))

# test case 2 
print(solution.maxArea([1,1]))