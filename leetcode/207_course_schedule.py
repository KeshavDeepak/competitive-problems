from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        indegs = [0] * numCourses
        graph = {node:[] for node in range(numCourses)}

        # build graph and indegs
        for b, a in prerequisites:
            graph[a].append(b)
            indegs[b] += 1
        
        # kahn time
        queue = deque([])

        # -- append all nodes with indegs of 0
        for node, indeg in enumerate(indegs):
            if indeg == 0:
                queue.append(node)
        
        while queue:
            curr = queue.popleft()

            # decrement neighbors indeg and append to queue if indeg becomes 0
            for nbr in graph[curr]:
                indegs[nbr] -= 1

                if indegs[nbr] == 0:
                    queue.append(nbr)
        
        # -- if any indegs of more than 0 exist, not possible
        for indeg in indegs:
            if indeg != 0:
                return False
        
        return True