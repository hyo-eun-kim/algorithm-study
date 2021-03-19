"""
## 뉴스 클러스터링
"""
from typing import *
import re
from collections import Counter


def solution(str1: str, str2: str) -> int:
    str1_lst = [str1[i:i+2].lower() for i in range(len(str1) - 1)
                if re.findall('(?i)[a-z]{2}', str1[i:i+2])]
    str2_lst = [str2[i:i + 2].lower() for i in range(len(str2) - 1)
                if re.findall('(?i)[a-z]{2}', str2[i:i + 2])]

    # 교집합
    intersection = sum((Counter(str1_lst) & Counter(str2_lst)).values())
    # 합집합
    union = sum((Counter(str1_lst) | Counter(str2_lst)).values())

    jaccard = 1 if union == 0 else intersection / union
    return int(jaccard * 65536)



if __name__ == '__main__':
    print(solution("FRANCE", "french"))
    print(solution("handshake", "shake hands"))