class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #MST-Prime's
        N = len(points) # map i: list of [cost,node]

        adj = {i:[] for i in range(N)}
        for i in range(N):
            xi, yi = points[i]
            for j in range(i+1, N):
                xj, yj = points[j]
                dist = abs(xi-xj) + abs(yi-yj)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        # Prime's
        count = 0 
        minHeap = [[0,0]]
        visited = set()
        while len(visited) < N:
            cost,i = heapq.heappop(minHeap)
            if i in visited:
                continue 
            count += cost
            visited.add(i)
            for neighCost,neigh in adj[i]:
                if neigh not in visited:
                    heapq.heappush(minHeap, [neighCost,neigh])
        return count
        