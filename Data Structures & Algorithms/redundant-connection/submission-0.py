class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        preMap = {i: [] for i in range(1, len(edges) + 1)}

        
        def dfs(node, target, visited):
            if node == target:
                return True  
            
            visited.add(node)
            
            for nodeNeighbor in preMap[node]:
                if nodeNeighbor not in visited:
                    if dfs(nodeNeighbor, target, visited):
                        return True
            return False
        
        
        for n1, n2 in edges:
            visited = set()
            
           
            if dfs(n1, n2, visited):
                return [n1, n2]
            
           
            preMap[n1].append(n2)
            preMap[n2].append(n1)
            
        return []