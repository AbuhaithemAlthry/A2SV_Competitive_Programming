class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i!=j and (((bombs[i][0]-bombs[j][0])**2 + (bombs[i][1]-bombs[j][1])**2)**0.5) <= bombs[i][2]:
                        graph[i].append(j)
        
        def dfs(node):
            for neighbour in graph[node]:
                if not neighbour in visited:
                    visited.add(neighbour)
                    dfs(neighbour)
        
        max_=0
        for i in range(len(bombs)):
            visited = {i}
            dfs(i)
            max_ = max(max_, len(visited))
        return max_
        