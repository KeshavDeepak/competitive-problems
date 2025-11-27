class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid-1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1
