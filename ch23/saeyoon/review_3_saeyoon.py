"""
## 395. Longest Substring with At Least K Repeating Characters

Given a string s and an integer k,
return the length of the longest substring of s
such that the frequency of each character in this substring
is greater than or equal to k.
"""


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)
