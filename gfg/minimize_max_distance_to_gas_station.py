import math

class Solution:
    def minMaxDist(self, stations, k):
        n = len(stations)

        # ------------ base case
        if n == 1: return 0
        
        # ------------ main case
        # find left and right
        left = 0
        right = -math.inf
        
        for i in range(1, n):
            gap = stations[i] - stations[i-1]
            
            right = max(right, gap)
        
        # binary search
        while (right - left) > 1e-6:
            maximum = (left + right) / 2.0
            
            # print(left, right, maximum)
            
            # is it possible to achieve max
            new = 0
            
            for i in range(1, n):
                gap = stations[i] - stations[i-1]
                
                new += math.ceil(gap / maximum) - 1
                
            if new <= k: # it is possible
                right = maximum
            else: # not possible
                left = maximum
        
        return right
