# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# main code
from collections import deque

class Solution:
    def maxLevelSum(self, root) -> int:
        queue = deque([root])
        answer = float('-inf')
        level = 1
        max_level = -1

        while queue:
            level_sum = sum([x.val for x in queue]) 
            if level_sum > answer:
                answer = level_sum
                max_level = level

            curr_nodes = len(queue)

            for _ in range(curr_nodes):
                node = queue.popleft()

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
            level += 1
        
        return max_level
