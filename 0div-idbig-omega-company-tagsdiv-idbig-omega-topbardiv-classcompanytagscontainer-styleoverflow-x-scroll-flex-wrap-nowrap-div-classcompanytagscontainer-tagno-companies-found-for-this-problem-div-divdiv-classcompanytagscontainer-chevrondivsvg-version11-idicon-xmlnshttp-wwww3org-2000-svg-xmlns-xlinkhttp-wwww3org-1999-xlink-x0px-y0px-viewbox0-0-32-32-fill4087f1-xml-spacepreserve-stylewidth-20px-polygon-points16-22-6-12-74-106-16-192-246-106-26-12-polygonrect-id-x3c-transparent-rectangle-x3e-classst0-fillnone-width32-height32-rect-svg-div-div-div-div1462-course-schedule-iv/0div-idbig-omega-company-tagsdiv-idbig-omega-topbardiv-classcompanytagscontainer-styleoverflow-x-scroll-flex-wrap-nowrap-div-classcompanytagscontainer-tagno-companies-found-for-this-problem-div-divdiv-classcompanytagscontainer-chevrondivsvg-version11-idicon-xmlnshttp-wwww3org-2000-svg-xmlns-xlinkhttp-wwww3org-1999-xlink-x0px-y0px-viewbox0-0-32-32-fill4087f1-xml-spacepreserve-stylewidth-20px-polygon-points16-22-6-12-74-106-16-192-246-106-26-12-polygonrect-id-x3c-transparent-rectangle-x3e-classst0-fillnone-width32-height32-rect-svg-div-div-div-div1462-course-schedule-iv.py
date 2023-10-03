class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        isReachable = [[False] * numCourses for _ in range(numCourses)]

        # Initialize the isReachable matrix based on prerequisites
        for st, en in prerequisites:
            isReachable[st][en] = True

        # Floyd-Warshall algorithm to calculate transitive closure
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    isReachable[i][j] = isReachable[i][j] or (isReachable[i][k] and isReachable[k][j])

        return [isReachable[i][j] for i, j in queries]