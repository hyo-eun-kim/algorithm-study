'''
https://leetcode.com/problems/implement-trie-prefix-tree/
Trie 구현하기 (Prefix Tree)

runtime 124ms (faster than 94%)
memory 27.7MB (less than 91%)
'''

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.trie
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur['end'] = True
        print(self.trie)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.trie
        for char in word:
            if char in cur:
                cur = cur[char]
            else:
                return False
        return True if 'end' in cur else False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.trie
        for char in prefix:
            if char in cur:
                cur = cur[char]
            else:
                return False
        return True
        

if __name__ == "__main__":
    # Your Trie object will be instantiated and called as such:

    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))    # returns true
    print(trie.search("app"))      # returns false
    print(trie.startsWith("app"))  # returns true
    trie.insert("app")
    print(trie.search("app"))      #return true