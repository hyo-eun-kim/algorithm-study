"""
## 16-1. 트라이 구현

트라이의 insert, search, startsWith 메소드를 구현하라.
"""

class TrieNode:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for i in prefix:
            if i not in node.children:
                return False
            node = node.children[i]
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple")) # True
    print(trie.search("app")) # False
    print(trie.startsWith("app")) # True
    trie.insert("app")
    print(trie.search("app")) # True