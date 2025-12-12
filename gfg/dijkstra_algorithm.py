import heapq

class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # make graph
        graph = {node : [] for node in range(V)}
        
        for start, end, dist in edges:
            graph[start].append((dist, end))
            graph[end].append((dist, start))
        
        # initialize dists
        dists = [float('inf')] * V
        
        dists[src] = 0
        
        # initialize heap for maintaning pq (dist, node)
        queue = [(0, src)]
        heapq.heapify(queue)
        
        #
        visited = set()
        
        # dijkstra on queue until empty
        while queue:
            # get the smallest element
            dist, node = heapq.heappop(queue)
            
            # if an old worse route, ignore
            if dist > dists[node]: continue
        
            # mark as visited
            visited.add(node)
            
            # explore neighbors and update their dist if smaller
            for dist, neighbor in graph[node]:
                if (dist + dists[node]) < dists[neighbor]: # update neighbor's dist
                    dists[neighbor] = (dist + dists[node])
                        
                    heapq.heappush(queue, (dists[neighbor], neighbor))
                    
        # 
        return dists
        
