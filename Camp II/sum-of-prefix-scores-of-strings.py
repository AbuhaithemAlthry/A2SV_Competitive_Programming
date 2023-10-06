class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = [ None for _ in range(26) ]

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            index = ord(char) - ord('a') 
            if not node.children[index]:
                node.children[index] = TrieNode() 
            node = node.children[index]
            node.count += 1
    def sum_(self,word: str):
        node = self.root
        res = 0
        for char in word:
            index = ord(char) - ord('a')
            res += node.children[index].count
            node = node.children[index]
        return res
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        ans = []
        for word in words:
            ans.append(trie.sum_(word))
        return ans
