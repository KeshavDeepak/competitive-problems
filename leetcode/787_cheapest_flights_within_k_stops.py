import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dists = [float('inf')] * n
        dists[src] = 0

        for _ in range(k+1):
            tmp = dists[:]

            # relax all edges
            for start, end, price in flights:
                if dists[start] + price < tmp[end]:
                    tmp[end] = dists[start] + price
            
            dists = tmp[:]

        return dists[dst] if dists[dst] != float('inf') else -1
