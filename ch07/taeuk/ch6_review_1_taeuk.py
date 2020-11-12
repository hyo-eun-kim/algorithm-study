'''
Shortest Palindrome

Given a string s, you can convert it to a palindrome by adding characters in front of it. 
Find and return the shortest palindrome you can find by performing this transformation.
'''

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        reverse_s = s[::-1]
        for i in range(len(s)+1):
            if s.startswith(reverse_s[i:]):
                return reverse_s[:i] + s
