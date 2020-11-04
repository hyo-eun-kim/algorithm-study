'''
04. 가장 흔한 단어

금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며，구두점 (마침표, 쉽표 등)또한 무시한다.
'''

import collections

# 내 풀이
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 정규표현식을 이용해 문자를 제외하고 모두 공백처리
        # 전체 문자를 소문자로 바꾸고 공백을 기준으로 split
        paragraph = re.sub('[^\w]',' ',paragraph).lower().split()
        # banned에 포함되어 있지 않은 단어 제거
        words = [word for word in paragraph if word not in banned]
        # Counter를 이용하여 빈도 계산 후 가장 많이 등장한 단어 하나 추출
        common_word = collections.Counter(words).most_common(1)[0][0]
        return common_word

# 모범답안
'''
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]'， paragraph)
            .lower( ). spllt( )
                if word not in banned]
        counts = collections.Counter(words)
        # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
        return counts.most_common(1)[0][0]
'''