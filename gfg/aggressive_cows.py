class Solution:
    def aggressiveCows(self, stalls, k):
        stalls.sort()
        
        left = 1
        right = (stalls[-1]-stalls[0]) // (k-1)
        
        answer = left
        
        while left <= right:
            target_dist = (left + right) // 2
            
            # is it possible to achieve target
            cows = k - 1
            prev_i = 0
            curr_i = 1
            
            while curr_i <= len(stalls)-1 and cows > 0:
                if stalls[curr_i] >= stalls[prev_i] + target_dist: # place cow here
                    prev_i = curr_i
                    cows -= 1
                
                curr_i += 1
            
            # check if target has been reached or not
            if cows == 0: # hurray -- see if a bigger distance is possible or not
                answer = target_dist
                left = target_dist + 1
            else: # target not possible, try a smaller distance
                right = target_dist - 1
        
        return answer
