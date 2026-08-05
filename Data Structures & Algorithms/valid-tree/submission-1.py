class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        preMap  = {i:[] for i in range(n)}
        visited = set()
        for n1, n2 in edges:
            preMap[n1].append(n2)
            preMap[n2].append(n1)
        def dfs (edge, prev):
            if edge in visited:
                return False
            visited.add(edge)
            for nodeEdge in preMap[edge]:
                if nodeEdge == prev:
                    continue
                if not dfs(nodeEdge, edge):
                    return False
            return True
    
        return dfs(0,-1) and n == len(visited)
        