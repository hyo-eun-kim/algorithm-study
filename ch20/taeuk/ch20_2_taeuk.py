'''
76. 부분 문자열이 포함된 최소 윈도우

문자열 S와 T를 입력받아 O(n)에 T의 모든 문자가 포함된 S의 최소 윈도우를 찾아라.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:

Input: s = "a", t = "a"
Output: "a"

'''

# 투 포인터, 슬라이딩 윈도우를 이용한 풀이
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 필요한 문자 각각의 개수
        need = collections.Counter(t)
        # 필요한 문자의 전체 개수
        missing = len(t)
        left = start = end = 0
        
        # 오른쪽 포인터 이동
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1
            
            if missing == 0:
                while left <right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                
                if not end or right - left <= end - start:
                    start, end = left, right
                    need[s[left]] += 1
                    missing += 1
                    left += 1
        return s[start:end]
    # 116 ms