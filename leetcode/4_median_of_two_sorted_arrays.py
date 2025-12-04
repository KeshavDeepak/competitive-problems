import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)

        # base cases
        if n == 0: return median(nums2)
        if m == 0: return median(nums1)

        # main case
        left = 0
        right = min(n, m)
        arr = nums1 if right == n else nums2
        arr_2 = nums2 if arr == nums1 else nums1
        half_size = (n+m) // 2

        n = len(arr)
        m = len(arr_2)

        while left <= right:
            # find the splitting points
            take_from_arr = (left + right) // 2
            take_from_arr2 = (half_size - take_from_arr)

            # find the values at the splits
            l1 = arr[take_from_arr-1] if take_from_arr != 0 else -math.inf
            r1 = arr[take_from_arr] if take_from_arr != n else math.inf

            l2 = arr_2[take_from_arr2-1] if take_from_arr2 != 0 else -math.inf
            r2 = arr_2[take_from_arr2] if take_from_arr2 != m else math.inf

            print(l1, r1, l2,r2, take_from_arr, take_from_arr2)

            # verify if split is valid or not
            if l1 > r2: 
                right = take_from_arr - 1
                continue
            
            if l2 > r1:
                left = take_from_arr + 1
                continue
            
            # split is valid if reached this line of code
            return (max(l1, l2) + min(r1, r2)) / 2 if (n+m) % 2 == 0 else min(r1, r2)

        return 0.0
