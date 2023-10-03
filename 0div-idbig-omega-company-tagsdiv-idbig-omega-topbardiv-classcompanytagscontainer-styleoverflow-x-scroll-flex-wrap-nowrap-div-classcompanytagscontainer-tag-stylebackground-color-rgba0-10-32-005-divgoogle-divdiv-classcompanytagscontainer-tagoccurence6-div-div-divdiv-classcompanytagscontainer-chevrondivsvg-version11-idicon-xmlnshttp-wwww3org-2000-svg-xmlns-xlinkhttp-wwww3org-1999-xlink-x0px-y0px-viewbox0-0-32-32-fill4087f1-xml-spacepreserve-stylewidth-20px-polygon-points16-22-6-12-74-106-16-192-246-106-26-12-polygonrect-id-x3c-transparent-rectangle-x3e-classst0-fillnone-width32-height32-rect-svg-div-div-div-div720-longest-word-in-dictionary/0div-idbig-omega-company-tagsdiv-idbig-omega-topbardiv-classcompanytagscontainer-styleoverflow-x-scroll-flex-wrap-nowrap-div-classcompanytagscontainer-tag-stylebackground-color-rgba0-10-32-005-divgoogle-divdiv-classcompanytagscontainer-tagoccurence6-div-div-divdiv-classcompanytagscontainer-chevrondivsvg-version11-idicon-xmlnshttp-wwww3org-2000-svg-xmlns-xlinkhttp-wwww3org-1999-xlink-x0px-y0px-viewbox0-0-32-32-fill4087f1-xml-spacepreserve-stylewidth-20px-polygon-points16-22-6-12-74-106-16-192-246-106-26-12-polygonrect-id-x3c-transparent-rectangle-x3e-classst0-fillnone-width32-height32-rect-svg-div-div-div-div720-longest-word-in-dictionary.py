class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.ret = ""

    def insert(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.isWord = True

class Solution:
    def longestWord(self, words):
        def dfs(node, path):
            if not node.isWord:
                return
            if len(path) > len(self.ret):
                self.ret = "".join(path)
            for letter in node.children:
                dfs(node.children[letter], path + [letter])

        words.sort()
        trie = Trie()
        trie.root.isWord = True
        for word in words:
            trie.insert(word)
        self.ret = ""
        dfs(trie.root, [])
        return self.ret