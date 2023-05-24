class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        root = {chr(i+97):chr(i+97) for i in range(26)}
        rank = {chr(i+97):i for i in range(26)}
        def find(x):
            while x!= root[x]:
                x=root[x]
            return x
        def union(x,y):
            rootX=find(x)
            rootY=find(y)
            if rank[rootX] > rank[rootY]:
                root[rootX]=root[rootY]
            elif rank[rootX] <= rank[rootY]:
                root[rootY]=root[rootX]
        def connected(x,y):
            return find(x)==find(y)
        for equation in equations:
            if equation[1:3] == '==':
                union(equation[0],equation[-1])
        for equation in equations:
            if equation[1:3] == '!=':
                if find(equation[0])==find(equation[-1]):
                    return False
        return True