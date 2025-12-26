class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        lis = []

        for num in nums:
            # find place to insert/replace
            # -- if no element in lis, add num directly
            if len(lis) == 0: 
                lis.append(num)
                continue

            # -- if elems exist, then find position to add num in
            # -- if num > lis[-1], append to lis
            if num > lis[-1]: 
                lis.append(num)
                continue

            # -- if not, find place inside lis
            left = 0
            right = len(lis) - 1
            mid = 0

            while left <= right:
                mid = (left + right) // 2

                if lis[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
            
            # -- add num to position
            lis[left] = num
        
        return len(lis)