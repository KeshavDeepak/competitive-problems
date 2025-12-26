class Solution:
    def twoSums(self, nums, left_pointer, right_pointer, total):
        two_sums = []

        while left_pointer < right_pointer:
            left = nums[left_pointer]
            right = nums[right_pointer]
            curr_total = left + right

            if curr_total == total:
                two_sums.append([left, right])
                
                # move left pointer until a new number is reached or termination
                left_pointer += 1

                while left_pointer < right_pointer and \
                    nums[left_pointer] == nums[left_pointer-1]:
                    left_pointer += 1

            elif curr_total < total:
                left_pointer += 1
            else: # curr_total > total
                right_pointer -= 1
        
        return two_sums

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        three_sums = []
        n = len(nums)

        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            two_sums = self.twoSums(nums, i+1, n-1, -1*nums[i])

            for two_sum in two_sums:
                three_sums.append([nums[i], *two_sum])
        
        return three_sums


