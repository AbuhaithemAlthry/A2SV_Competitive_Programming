class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        def builder(edges):
            dic=defaultdict(list)
            for s,d in edges:
                dic[s].append(d)
                dic[d].append(s)
            return dic
        graph=builder(edges)
        max_= 0
        ans = 0
        for i,arr in graph.items():
            if max_< len(arr):
                max_ = len(arr)
                ans = i
        return ans