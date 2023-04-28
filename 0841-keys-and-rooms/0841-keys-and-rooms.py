class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        
        def bfs(node):
            queue = deque([node])

            while queue:
                print(queue)
                node = queue.popleft()

                for neighbour in rooms[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
        
        bfs(0)
        return len(visited)==len(rooms)