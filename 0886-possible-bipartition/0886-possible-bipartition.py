class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        color = [-1] * (n + 1) 
        def dfs(node, node_color):
            color[node] = node_color
            for neighbor in graph[node]:
                if color[neighbor] == color[node]: 
                    return False
                if color[neighbor] == -1:
                    if not dfs(neighbor, 1 - node_color):
                        return False
            return True
        
        graph = defaultdict(list)
        for dislike in dislikes:
            graph[dislike[0]].append(dislike[1])
            graph[dislike[1]].append(dislike[0])

        for i in range(1, n + 1):
            if color[i] == -1:
                # For each pending component, run DFS.
                if not dfs(i, 1):
                    # Return false, if there is conflict in the component.
                    return False
        
        return True