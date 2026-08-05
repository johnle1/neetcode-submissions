class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each class an empty list
        preMap = {i:[] for i in range(numCourses)}
        visited = set()
        for course, requires in prerequisites:
            preMap[course].append(requires)

        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs] == []:
                return True
            
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            preMap[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True


        

        