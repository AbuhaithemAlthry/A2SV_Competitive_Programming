class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.score = 0

class MapSum(object):
    def __init__(self):
        self.map = defaultdict(int)
        self.root = TrieNode()

    def insert(self, key, val):
        delta = val - self.map[key]
        self.map[key] = val
        cur = self.root
        cur.score += delta
        for char in key:
            cur = cur.children.setdefault(char, TrieNode())
            cur.score += delta

    def sum(self, prefix):
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        return cur.score
