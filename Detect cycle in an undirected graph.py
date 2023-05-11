from typing import List
from collections import defaultdict
class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        #Code here
        visited = set()
        def dfs(node,parent):
            for child in adj[node]:
                if (child != parent) and (child not in visited):
                    visited.add(child)
                    if not dfs(child,node):
                        return False
                elif (child != parent) and (child in visited):
                    return False
            return True
                
            
        
        for i in range(V):
            if i not in visited:
                visited.add(i)
                if not dfs(i,-1):
                    return True
        return False

#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
