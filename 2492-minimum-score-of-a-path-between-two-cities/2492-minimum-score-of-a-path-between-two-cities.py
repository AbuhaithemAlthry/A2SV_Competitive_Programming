class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for st,en,di in roads:
            graph[st].append(en)
            graph[en].append(st)
        def preprocess(city):
            for city in graph:
                components[city] = set([city])
            for city in graph:
                for neighbor in graph[city]:
                    if neighbor not in components:
                        continue
                    if components[city] is not components[neighbor]:
                        components[city] |= components[neighbor] # union set
                        for c in components[neighbor]:
                            components[c] = components[city] # set references
            return components
        components = defaultdict(set)
        preprocess(1)
        min_=float(inf)
        for st,en,di in roads:
            if st in components[1] and en in components[1]:
                min_=min(min_,di)
        return min_