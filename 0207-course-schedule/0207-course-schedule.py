class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        incoming = [0 for _ in range(numCourses)]
        queue = deque()
        
        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming[course]+=1
            
        for course in range(numCourses):
            if incoming[course] == 0:
                queue.append(course)
        while queue:
            course = queue.popleft()
            for neighbor in graph[course]:
                incoming[neighbor] -= 1
                if incoming[neighbor] == 0:
                    queue.append(neighbor)
        return True if sum(incoming)==0 else False