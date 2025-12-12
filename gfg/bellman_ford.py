#User function Template for python3

class Solution:
    def bellmanFord(self, V, edges, src):
        # build dists
        dists = [float('inf')] * V
        dists[src] = 0
        
        # bellman-ford
        for round in range(V):
            tmp = dists[:]
            
            # relax all edges
            for start, end, dist in edges:
                if dists[start] + dist < tmp[end]:
                    tmp[end] = dists[start] + dist
                
            # save at one-but-last
            if round == V-2:
                old_dists = tmp
            
            dists = tmp
        
        # negative cycle?
        if dists != old_dists: return [-1]
        
        #
        return [dist if dist != float('inf') else int(1e8) for dist in dists] 
            
