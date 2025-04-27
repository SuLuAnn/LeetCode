class TreeNode:
    def __init__(self):
        self.suffix_nodes = [None] * 27

class Trie:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not node.suffix_nodes[index]:
                node.suffix_nodes[index] = TreeNode()
            node = node.suffix_nodes[index]
        node.suffix_nodes[26] = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not node.suffix_nodes[index]:
                return False
            node = node.suffix_nodes[index]
        return node.suffix_nodes[26] is True

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if not node.suffix_nodes[index]:
                return False
            node = node.suffix_nodes[index]
        return True