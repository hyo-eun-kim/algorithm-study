'''
57. 팰린드롬 페어

단어 리스트에서 words[i] + words[j]가 팰린드롬이 되는 모든 인덱스 조합 (i, j)를 구하라.

Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]
'''
# 브루트 포스
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(check):
            return check == check[::-1]
        
        output = []
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i == j:
                    continue
                if is_palindrome(word1 + word2):
                    output.append([i,j])
        return output
    
    # timeout...
    
# 트라이 구현
class TrieNode:
    def __init__(self):
        self.word_id = -1
        self.children = collections.defaultdict(TrieNode)
        self.palindrome_word_ids = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def is_palindrome(self,check: str) -> bool:
            return check == check[::-1]

    def insert(self, index, word: str) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            print(word[0:len(word) - i])
            if self.is_palindrome(word[0:len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
            node.val = char
        node.word_id = index

    def search(self, index, word: str) -> bool:
        result = []
        node = self.root
        
        while word:
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])
            
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])
            
        return result
            
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()
        
        for i, word in enumerate(words):
            trie.insert(i, word)
            
        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))
            
        return results
    # 1268 ms