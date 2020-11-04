'''
05. 그룹 애너그램

문자열 배열을 받아 애너그램 단위로 그룹핑하라.
'''

import collections

# 내 풀이
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 없는 key를 넣어도 에러가 나지않게 defaultdict으로 만듬
        anagrams = collections.defaultdict(list)
        for word in strs:
            # 각 단어를 정렬해 key로 삼고 원래의 단어를 value로 넣어줌
            anagrams[''.join(sorted(list(word)))].append(word)
        return list(anagrams.values())

# 모범답안
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(list(word)))].append(word)
        return anagrams.values()
'''