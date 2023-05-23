class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        root = {chr(i+97):chr(i+97) for i in range(26)}
        rank = {chr(i+97) : i for i in range(26)}
        
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        
        def union(x):
            rootX = find(s1[x])
            rootY = find(s2[x])
            if rootX != rootY:
                if rank[rootX] < rank[rootY]:
                    root[rootY] = rootX
                elif  rank[rootY] <= rank[rootX]:
                    root[rootX] = rootY

        
        for i in range(len(s1)):
            union(i)
        
        soln = []
        for j in (baseStr):
            soln.append(find(j))
        
        return ''.join(soln)