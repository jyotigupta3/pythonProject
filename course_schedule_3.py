from typing import List


class Solution:

    def scheduleCourse(self, courses: List[List[int]]) -> int:
        array = sorted(courses, key = lambda x:x[1])
        priorityQueue = []
        time = 0

        for course in array:
            if course[0]<=course[1]:

                if course[0]+time <= course[1]:
                    priorityQueue.append(course[0])
                    time += course[0]
                else:
                    traced_course = max(priorityQueue)
                    if course[0] < traced_course:
                        priorityQueue.remove(traced_course)
                        priorityQueue.append(course[0])
                        time -= traced_course
                        time += course[0]
        return len(priorityQueue)


if __name__ == "__main__":
    res = Solution().scheduleCourse(courses=[[5,5],[4,6],[2,6]])
    print(res)

