from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [False] * numCourses
        # map each course to prereq list
        graph = {i: [] for i in range(numCourses)}

        # visitset = all courses along the current DFS path
        visitSet = set()

        def DFS(crs):
            if crs in visitSet:
                return False
            if graph[crs] == []:
                return True

            visitSet.add(crs)
            for pre in graph[crs]:
                if not DFS(pre): return False
            visitSet.remove(crs)
            graph[crs] = []
            return True

        for course in prerequisites:
            crs, pre = course
            graph[crs].append(pre)

        for crs in range(numCourses):
            if not DFS(crs): return False

        return True


if __name__ == "__main__":
    res = Solution().canFinish(numCourses=3, prerequisites=[[1,0],[0,2]])
    res = Solution().canFinish(numCourses=2, prerequisites=[[1,0],[0,1]])
    print(res)