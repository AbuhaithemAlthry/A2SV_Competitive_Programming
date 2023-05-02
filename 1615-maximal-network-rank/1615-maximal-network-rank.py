class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for st,en in roads:
            graph[st].append(en)
            graph[en].append(st)
        max_=0
        for key1,val in graph.items():
            for key2,val in graph.items():
                if key1 != key2:
                    if (key2 in graph[key1]):
                        max_ = max((len(graph[key1])+len(graph[key2])-1),max_)
                    else:
                        max_ = max((len(graph[key1])+len(graph[key2])),max_)
        return max_