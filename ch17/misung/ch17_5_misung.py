# 유효한 애너그램
# t가 s의 애너그램인지 판별하라.
from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s)==sorted(t)

    def isAnagram2(self, s, t):
        hash_table = dict(Counter(s))
        hash_table2 = dict(Counter(t))
        return hash_table == hash_table2