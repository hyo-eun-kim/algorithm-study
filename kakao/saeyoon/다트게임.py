"""
## 다트 게임
"""
from typing import *
import re


def solution(dartResult: str) -> int:
    score = 0
    chances = re.findall("[0-9]{1,2}[SDT][*#]?", dartResult)

    num = [int(re.findall("[0-9]{1,2}", i)[0]) for i in chances]

    bonus_str = [re.findall("[SDT]", i)[0] for i in chances]
    dic = {'S': 1, 'D': 2, 'T': 3}
    bonus = [dic.get(i) for i in bonus_str]

    option_str = [re.findall("[*#]", i)[0] if len(re.findall("[*#]", i)) != 0 else 1
                  for i in chances]
    dic2 = {"*": 2, "#": -1, 1: 1}
    option = [dic2.get(i) for i in option_str]

    for i in range(3):
        if option_str[i] == "*":
            if i == 0:
                score += (num[i] ** bonus[i]) * option[i]
            else:
                score += (num[i-1] ** bonus[i-1]) * option[i-1]
                score += (num[i-1] ** bonus[i-1]) * option[i-1] * option[i]
                score += (num[i] ** bonus[i]) * option[i]
        else:
            score += (num[i] ** bonus[i]) * option[i]

    return score


if __name__ == '__main__':
    print(solution("1S2D*3T"))