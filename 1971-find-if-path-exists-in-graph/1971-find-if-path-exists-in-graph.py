class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if len(edges)==0:
            return True
        graph=defaultdict(list)
        for st,en in edges:
            graph[st].append(en)
            graph[en].append(st)
        
        def preprocess(city):
            # components = {}
            # to avoid if conditions, let’s put all city in their own set
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
        
        def query(component, city1, city2):
            return city1 in component and city2 in component
        
       
        components = defaultdict(set)
        for i in range(len(graph)):
            if i not in components:
                preprocess(i)
                if query(components[i], source, destination):
                    return True
        return False
