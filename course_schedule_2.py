from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = {i: [] for i in range(numCourses)}
        visitSet, cycle = set(), set()
        result = []

        for course in prerequisites:
            crs, pre = course
            graph[crs].append(pre)

        def DFS(crs):
            if crs in cycle:
                return False
            if crs in result:
                return True
            cycle.add(crs)
            for pre in graph[crs]:
                if not DFS(pre):
                    return False
            cycle.remove(crs)
            result.append(crs)
            return True

        for crs in range(numCourses):
            if not DFS(crs):
                return []
        return result

if __name__ == "__main__":
    res = Solution().findOrder(numCourses=4, prerequisites=[[1,0],[2,0],[3,1],[3,2]])
    # res = Solution().findOrder(numCourses=2, prerequisites=[[1,0],[0,1]])
    print(res)