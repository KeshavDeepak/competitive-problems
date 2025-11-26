class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)

        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            print(left, right, mid)

            # if mid is target, voila
            if nums[mid] == target:
                return True
            
            # if left=right=mid
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue
            
            # find sorted half and keep/eliminate it
            if nums[left] <= nums[mid]: # left half is sorted
                if nums[left] <= target <= nums[mid]: # target is here
                    right = mid - 1
                else: # target is not here
                    left = mid + 1
            else: # right half is sorted
                if nums[mid] <= target <= nums[right]: # target is here
                    left = mid + 1
                else: # target is not here
                    right = mid - 1

        #
        return False 

