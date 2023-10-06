class Trie:
    def __init__(self):
        self.root = {}
        self.m = 0

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            bit = int(char)
            if bit not in node:
                node[bit] = {}
            node = node[bit]

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        for i in nums:
            word = "{:032b}".format(i)
            trie.insert(word)

        maxXOR = 0
        for i in nums:
            word = "{:032b}".format(i)
            node = trie.root
            t = ""
            for ch in word:
                bit = int(ch)
                if 1-bit in node:  
                    t += str(1-bit)
                    node = node[1-bit]
                else:
                    t += ch
                    node = node[bit]
            maxXOR = max(maxXOR, int(t, 2) ^ i)

        return maxXOR
