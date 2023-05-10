class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        incoming = [0] * (n)
        queue = deque()
        res = [[] for i in range(n)]
        
        for pre,sour in edges:
            graph[pre].append(sour)
            incoming[sour]+=1
          
        for i in range(len(incoming)):
            if incoming[i] == 0:
                queue.append(i)
                
        anc = []
        while queue:
            pop = queue.popleft()
            for neigbour in graph[pop]:
                res[neigbour].append(pop)
                for i in res[pop]:
                    if i not in res[neigbour]:
                        res[neigbour].append(i)
                incoming[neigbour]-=1
                if (incoming[neigbour]==0):
                    queue.append(neigbour)
        return [ sorted(res[i]) for i in range(len(res))]
                    