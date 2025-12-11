from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degs = [0] * numCourses
        graph = {course : [] for course in range(numCourses)}

        # go through prerequisites to both build graph and compute in degrees
        for b, a in prerequisites:
            # update b's in degree
            in_degs[b] += 1

            # update a's neighbors
            graph[a].append(b)
        
        # initialize queue with nodes of in_degree=0
        queue = deque([course for course, in_deg in enumerate(in_degs) if in_deg == 0])
        answer = []

        # topologically sort and store nodes in order
        while queue:
            course = queue.popleft()
            
            answer.append(course)

            # add neighbors of course to queue if in_degree is 0
            for neighbor in graph[course]:
                # decrement neighbor's in degree
                in_degs[neighbor] -= 1

                # if 0, add to queue
                if in_degs[neighbor] == 0:
                    queue.append(neighbor)
        
        # 
        return answer if len(answer) == numCourses else []
            

