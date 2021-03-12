# 분할정복
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
# Given a string s and an integer k, return the length of the longest substring of s such that 
# the frequency of each character in this substring is greater than or equal to k.

# Input: s = "aaabb", k = 3
# Output: 3
# Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

from collections import Counter

class Solution:
    def longestSubstring(self, s, k):
        if len(s) == 0 or k > len(s):
            return 0

        c = Counter(s)
        sub1, sub2 = "", ""
        for i, letter in enumerate(s):
            if c[letter] < k: # k보다 빈도수가 작으면 => 왼쪽 오른쪽 나눠서 다시 substring 찾는다.
                # print(letter)
                # print(s[:i])
                sub1 = self.longestSubstring(s[:i], k) # 왼쪽 
                sub2 = self.longestSubstring(s[i+1:], k) # 오른쪽 
                break
        else:
            return len(s) # 현재의 가장 긴 substring 길이 저장
            
        return max(sub1, sub2)