class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        preMap = {i:[] for i in range(n)}
        

        for n1, n2 in edges:
            preMap[n1].append(n2)
            preMap[n2].append(n1)

        visited = set()
        count = 0

        def dfs(node):
            visited.add(node)
            for edgeNei in preMap[node]:
                if edgeNei not in visited:
                    dfs(edgeNei)
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
                
        return count
            



        