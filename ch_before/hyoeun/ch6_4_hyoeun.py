# https://leetcode.com/problems/most-common-word/
# 금지된 단어를 제외한 나머지 단어 중 가장 흔하게 등장하는 단어를 출력하라.
# 대소문자를 구분하지 않으며 구두점 또한 고려되지 않는다.
from collections import Counter, defaultdict
import re


def solution_1(paragraph: str, banned: list):
    new_paragraph = ''
    new_paragraph_list = []

    # 전처리 과정
    # 문자를 제외한 나머지 제거 (정규식 사용해도 된다)
    for ch in paragraph:
        if ch.isalpha() or ch == ' ':
            new_paragraph += ch.lower()
        else:
            new_paragraph += " "

    # banned에 포함된 단어 제거
    for word in new_paragraph.split():
        if word not in banned:
            new_paragraph_list.append(word)

    counter = Counter(new_paragraph_list)
    return counter.most_common(1)[0][0]


def solution_2(paragraph: str, banned: list):
    # 정규식을 사용하여 alphabet 제외 공백으로 대체
    paragraph = re.sub('[^a-zA-Z]', ' ', paragraph)

    # 각 단어의 등장횟수 구하기 (defaultdict 사용)
    word_count_dict = defaultdict(int)
    for word in paragraph.split():
        word = word.lower()
        if word not in banned:
            word_count_dict[word] += 1

    # 등장횟수가 많은 단어 추출하기 위하여 정렬 사용
    word_count_dict = sorted(word_count_dict.items(), key=lambda x:x[1], reverse=True)
    return word_count_dict[0][0]
    # OR return max(word_count_dict, key=word_count_dict.get)



if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(solution_1(paragraph, banned))
    print(solution_2(paragraph, banned))
