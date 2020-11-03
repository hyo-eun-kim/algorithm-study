"""
## 6-4. 가장 흔한 단어

금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표) 또한 무시한다.
"""

import re
from collections import Counter, defaultdict


def solution(paragraph, banned):
    paragraph = paragraph.lower()
    paragraph = re.sub('[^a-z ]', '', paragraph)

    new_paragraph = []

    for word in paragraph.split():
        if word not in banned:
            new_paragraph.append(word)

    counts = Counter(new_paragraph)
    return counts.most_common(1)[0][0]


def solution_ans(paragraph, banned):
    words = [word for word in re.sub('[^\w]', ' ', paragraph).lower().split() if word not in banned]

    counts = Counter(words)
    return counts.most_common(1)[0][0]


if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"
    banned = ["hit"]
    print(solution(paragraph, banned))
    print(solution_ans(paragraph, banned))