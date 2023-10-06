class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None] * 26

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.is_end = True

    def search(self, word: str) -> bool:
        return self.searchNode(self.root, word)

    def searchNode(self, node: TrieNode, word: str) -> bool:
        if not word:
            return node.is_end

        char = word[0]
        if char == '.':
            for child in node.children:
                if child and self.searchNode(child, word[1:]):
                    return True
        else:
            index = ord(char) - ord('a')
            child = node.children[index]
            if child and self.searchNode(child, word[1:]):
                return True

        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
