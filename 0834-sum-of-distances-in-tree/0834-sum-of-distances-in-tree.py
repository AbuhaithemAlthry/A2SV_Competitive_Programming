class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # Our varaibles to store closer nodes and result
        result = [0] * n
        closer_nodes_count = [0] * n
        # keep track of our visited node
        seen = set()

        # Building our graph
        graph = [[] for _ in range(n)]      
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # DFS to calculate closer nodes count and our parent nodes S.O.D
        def dfs(curr):
            closer_nodes = 1
            for child in graph[curr]:
                if child not in seen:
                    seen.add(child)
                    child_nodes_count = dfs(child)
                    closer_nodes += child_nodes_count

                    # To first get the S.O.D of our root node, which is node 0 for this problem
                    result[0] += child_nodes_count

            closer_nodes_count[curr] = closer_nodes

            return closer_nodes

        def dfs2(curr):
            for child in graph[curr]:
                if child not in seen:
                    seen.add(child)              
                    # Formula: parent_root_sum - closer_nodes + further_nodes
                    result[child] = result[curr] - closer_nodes_count[child] + (n - closer_nodes_count[child])        
                    # current child node becomes a parent node
                    dfs2(child)


        seen.add(0)
        dfs(0)

        # reset seen for our dfs2 
        seen = set()   
        seen.add(0)

        # Using result[0] (node 0) as base to populate all the other nodes
        dfs2(0)
        return result