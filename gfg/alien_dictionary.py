from collections import deque

class Solution:
    def findOrder(self, words):
        n = len(words)
        
        # build graph and in_degs with all letters 
        graph = {}
        in_degs = {}
        
        for letter in set(''.join(words)):
            graph[letter] = set()
            in_degs[letter] = 0
        
        for i in range(1, n):
            # find first diff from prev word
            prev = words[i-1]
            curr = words[i]
            
            left = 0
            right = 0
            diff_found = False
            
            while left < len(prev) and right < len(curr):
                first = prev[left]
                second = curr[right]
                                
                if first != second:  # diff found
                    diff_found = True
                
                    if second not in graph[first]:
                        graph[first].add(second)
                        in_degs[second] += 1
                    
                    break
                        
            
                left += 1
                right += 1
            
            # if no difference is found and prev > curr, invalid
            if len(prev) > len(curr) and not diff_found:
                return ''
        
        # kahn to find ordering
        answer = ''
        
        # initialize queue with all in_degs of 0
        queue = deque([letter for letter in in_degs if in_degs[letter] == 0])
        
        while queue:
            letter = queue.popleft()
            answer += letter
            
            # add neighbors of letter in queue if their new in_deg is 0
            for neighbor in graph[letter]:
                in_degs[neighbor] -= 1
                if in_degs[neighbor] == 0:
                    queue.append(neighbor)
        
        return answer if len(answer) == len(graph) else ""
