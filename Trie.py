class TrieNode:
    def __init__(self):
        self.children = {}
        self.valid = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for l in word:
            if l not in node.children:
                node.children[l] = TrieNode()
            node = node.children[l]
        node.valid = True

    def search(self, word: str) -> bool:
        node = self.root
        for l in word:
            if l not in node.children:
                return False
            node = node.children[l]
        return node.valid

    def startWith(self, prefix: str) -> bool:
        node = self.root
        for l in prefix:
            if l not in node.children:
                return False
            node = node.children[l]
        return True
