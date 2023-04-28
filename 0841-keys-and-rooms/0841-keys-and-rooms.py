class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        queue = deque([0])
        while queue:
            print(queue)
            node = queue.popleft()

            for neighbour in rooms[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        return len(visited)==len(rooms)