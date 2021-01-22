# 트라이 구현
# 트라이의 insert , search, startswith 메소드를 구현하라.


# 트라이를 저장할 노드 
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode() #  트라이 노드의 처음

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word :
            node = node.children[char] # 다음 문자를 키로 하는 자식 노드 형태! 
        node.word = True # 도착하면 True 저장 
        print(node)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            if char not in node.children :
                return False
            node = node.children[char]

        return node.word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root 
        for char in prefix:
            if char not in node.children:
                return False

            node = node.children[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


