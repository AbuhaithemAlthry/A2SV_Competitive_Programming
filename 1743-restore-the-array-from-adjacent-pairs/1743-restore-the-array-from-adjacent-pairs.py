class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incoming = defaultdict(int)
        for st,en in adjacentPairs:
            graph[st].append(en)
            incoming[st] += 1
            
            graph[en].append(st)
            incoming[en] += 1
        val = []
        for no ,va in incoming.items():
            if va == 1:
                val.append(no)
        i = round(random.random())
        queue = deque([val[i]])
        order = [val[i]]
        visited = set([val[i]])
        while queue:
            cur = queue.popleft()
            incoming[cur]-=1
            for child in graph[cur]:
                if child not in visited:
                    visited.add(child)
                    order.append(child)
                    incoming[child]-=1
                    if incoming[child] == 1:
                        queue.append(child)
        return (order)
                    