"""
## 6-5. 그룹 애너그램

문자열 배열을 받아 애너그램 단위로 그룹핑하라

* 애너그램: 일종의 언어유희로 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것.
예를 들어 '문전박대'를 '대박전문'으로 바꿔 부르는 단어 등이 있다.
"""

import re
from collections import defaultdict


def solution(strs):
    anagrams = defaultdict(list)

    for s in strs:
        anagrams[''.join(sorted(s))].append(s)
    return list(anagrams.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution(strs))