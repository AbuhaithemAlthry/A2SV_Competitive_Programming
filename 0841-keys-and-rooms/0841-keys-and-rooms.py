class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False]*len(rooms)
        def dfs(node):
            visited[node] = True
            for neighbour in rooms[node]:
                if not visited[neighbour]:
                    dfs(neighbour)
        dfs(0)
        return all(visited)