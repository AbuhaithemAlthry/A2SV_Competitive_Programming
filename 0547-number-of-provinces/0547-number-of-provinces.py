from collections import defaultdict
from typing import List

# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind(len(isConnected))

        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:  # Check for a connected province
                    uf.union(i, j)

        dic = defaultdict(int)
        for i in range(len(isConnected)):
            dic[uf.find(i)] += 1

        return len(dic)