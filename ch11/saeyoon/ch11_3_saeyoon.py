"""
## 11-3. 중복 문자 없는 가장 긴 부분 문자열

중복 문자가 없는 가장 긴 부분 문자열의 길이를 리턴하라.
"""
from typing import *


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 56 ms
        length = 0
        hashmap = {} # 각 문자의 현재 인덱스
        i = 0

        # [i, j] 범위로 늘려감
        for j in range(len(s)):
            # j번째 글자가 hasmap에 존재할 경우 i값을 j번째 글자 인덱스+1로 설정
            if s[j] in hashmap:
                i = max(hashmap[s[j]], i)
            length = max(length, j - i + 1)
            hashmap[s[j]] = j + 1

        return length

if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb")) # 3
    print(sol.lengthOfLongestSubstring("bbbbb")) # 1
    print(sol.lengthOfLongestSubstring("pwwkew")) # 3