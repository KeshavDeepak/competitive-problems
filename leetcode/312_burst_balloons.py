class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]
        self.dp = {}

        def f(left, right):
            # base cases
            if left > right:
                return 0

            if left == right:
                return nums[left-1] * nums[left] * nums[left+1]

            # if already memoized, use it instead
            if (left, right) in self.dp:
                return self.dp[(left, right)]

            # recursive case
            answer = 0

            # assume every balloon is burst last, calculate and choose maximal score
            curr = left

            while curr != right + 1:
                answer = max(
                    answer,
                    f(left, curr-1) + nums[left-1] * nums[curr] * nums[right+1] + f(curr+1, right)
                )

                curr += 1
            
            # memoize
            self.dp[(left, right)] = answer

            #
            return answer
        
        return f(1, len(nums)-2)