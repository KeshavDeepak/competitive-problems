import math

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [-math.inf] + nums + [-math.inf]

        left = 1
        right = len(nums) - 2

        while left <= right:
            mid = (left + right) // 2

            # is mid a peak element, if so, return it
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid-1
            
            # choose which side to go to
            if nums[mid-1] > nums[mid]:
                right = mid - 1
            else: # nums[mid+1]>nums[mid] is True
                left = mid + 1
