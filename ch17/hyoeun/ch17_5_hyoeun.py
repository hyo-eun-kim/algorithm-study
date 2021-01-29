'''
62. 유효한 애너그램
t가 s의 애너그램인지 판단하여라.
https://leetcode.com/problems/valid-anagram/
anagram? 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것 ex) eat -> tea
'''

from collections import defaultdict


class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        for char in s:
            s_dict[char] += 1
        for char in t:
            try:
                s_dict[char] -= 1
            except:
                return False
        return sum([i != 0 for i in s_dict.values()]) == 0


# 딕셔너리 객체끼리 == 연산하면, key, value 모두 동일하면 True 그렇지 않으면 False 반환!
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for char in s:
            s_dict[char] += 1
        for char in t:
            t_dict[char] += 1
        return s_dict == t_dict


# 책 풀이
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)