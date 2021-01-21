"""
## 16-2. 팰린드롬 페어

단어 리스트에서 words[i] + words[j]가 팰린드롬이 되는
모든 인덱스 조합 (i + j)를 구하라.
"""
from typing import *
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.index = -1
        self.palindromes_below = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def isPalindrome(self, word) -> bool:
        return word == word[::-1]

    def insert(self, word: str, index: int) -> None:
        node = self.root
        for i, c in enumerate(reversed(word)):
            if self.isPalindrome(word[0:len(word) - i]):
                node.palindromes_below.append(index)
            node = node.children[c]
        node.index = index

    def search(self, word: str, index: int) -> List:
        result = []
        node = self.root

        for i, c in enumerate(word):
            if node.index != -1 and node.index != index and self.isPalindrome(word[i:len(word)]):
                result.append([index, node.index])
            if c not in node.children:
                return result
            node = node.children[c]

        if node.index != -1 and node.index != index:
            result.append([index, node.index])

        for p_id in node.palindromes_below:
            result.append([index, p_id])

        return result


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        for i, word in enumerate(words):
            trie.insert(word, i)

        result = []
        for i, word in enumerate(words):
            result.extend(trie.search(word, i))

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
    print(sol.palindromePairs(["bat", "tab", "cat"]))
    print(sol.palindromePairs(["a", "abc", "aba", ""]))