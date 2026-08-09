class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        for crs, require in prerequisites:
            adj[crs].append(require)
        output =[]
        visited, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True 
            cycle.add(crs)
            for pre in adj[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return output

        
        