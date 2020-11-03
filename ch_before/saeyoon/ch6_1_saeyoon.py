"""
## 6-1. 유효한 팰린드롬

주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 안으며, 영문자와 숫자만을 대상으로 한다.

* 팰린드롬: 앞뒤가 똑같은 단어나 문장으로, 뒤집어도 같은 말이 되는 단어 또는 문장을 팰린드롬이라고 한다.
우리말 문장으로는 대표적으로 '소주 만 병만 주소' 같은 문장이 있다.
"""

import re

def solution(input):
    input = input.lower()
    input = re.sub('[^a-z0-9]', '', input)

    answer = (input == input[::-1])
    return answer

if __name__ == '__main__':
    input1 = "A man, a plan, a canal: Panama"
    input2 = "race a car"
    print(solution(input1)) # True
    print(solution(input2)) # False