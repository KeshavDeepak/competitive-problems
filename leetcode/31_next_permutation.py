class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # base cases
        if len(nums) == 1: return

        # find first dip
        for index in range(len(nums)-2, -1, -1):
            if nums[index] < nums[index+1]: # dip found
                # sort suffix list in ascending order
                nums[index+1:] = nums[-1:(len(nums)-index)*-1:-1]


                # find next greater element and swap with current index
                for suffix_index in range(index+1, len(nums)):
                    if nums[suffix_index] > nums[index]:
                        nums[index], nums[suffix_index] = nums[suffix_index], nums[index]
                        break
                
                break
        else:
            # if no dip found, default to lowest permutation
            nums[:] = nums[-1:-1*(len(nums)+1):-1]
                
                    