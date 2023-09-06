class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        answer = [-1] * n
        red = [set() for _ in range(n)]
        blue = [set() for _ in range(n)]

        for r in redEdges:
            red[r[0]].add(r[1])

        for b in blueEdges:
            blue[b[0]].add(b[1])

        visitedRed = [False] * n
        visitedBlue = [False] * n
        visitedRed[0] = True
        visitedBlue[0] = True

        queue = deque()
        queue.append((0, 0, "NONE"))

        while queue:
            node ,length, color = queue.popleft()
            if answer[node] == -1:
                answer[node] = length
            
            if color != 'RED':
                for child in red[node]:
                    if not visitedRed[child]:
                        visitedRed[child] = True
                        queue.append((child, length+1, "RED"))
            if color != 'BLUE':
                for child in blue[node]:
                    if not visitedBlue[child]:
                        visitedBlue[child]=True
                        queue.append((child, length+1, "BLUE"))

        return answer

