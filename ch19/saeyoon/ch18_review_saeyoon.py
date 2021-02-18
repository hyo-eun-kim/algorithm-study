"""
## 순위 검색

지원자가 지원서에 입력한 4가지의 정보와 획득한 코딩테스트 점수를
하나의 문자열로 구성한 값의 배열 info,
개발팀이 궁금해하는 문의조건이 문자열 형태로 담긴 배열 query가 매개변수로 주어질 때,

각 문의조건에 해당하는 사람들의 숫자를 순서대로 배열에 담아 return 하도록
solution 함수를 완성해 주세요.
"""
from copy import deepcopy
from itertools import combinations
import bisect


def solution(info, query):
    answer = []
    # 경우의 수 생성
    table = [
        ["cpp", "java", "python", "-"],
        ["backend", "frontend", "-"],
        ["junior", "senior", "-"],
        ["chicken", "pizza", "-"]
    ]

    cases = dict()
    # dfs로 모든 경우의 수 생성
    def make_cases(cnt, string):
        nonlocal cases
        if cnt == 4:
            cases[" and ".join(string)] = []
            return
        for t in table[cnt]:
            string.append(t)
            make_cases(cnt+1, string)
            string.pop()

    make_cases(0, [])

    for lst in info:
        *data, score = lst.split()
        for i in range(5):
            candidates = combinations(range(4), i)
            for position in candidates:
                copy_data = deepcopy(data)
                for idx in position:
                    copy_data[idx] = "-"
                # 조건에 해당하는 값 이진 검색 하여 해당 값 삽입
                bisect.insort_left(cases[" and ".join(copy_data)], int(score))

    for q in query:
        q, score = q.rsplit(maxsplit=1)[:-1][0], q.rsplit(maxsplit=1)[-1]
        idx = bisect.bisect_left(cases[q], int(score))
        answer.append(len(cases[q]) - idx)

    return answer


if __name__ == '__main__':
    print(solution(["java backend junior pizza 150",
                    "python frontend senior chicken 210",
                    "python frontend senior chicken 150",
                    "cpp backend senior pizza 260",
                    "java backend junior chicken 80",
                    "python backend senior chicken 50"],
                   ["java and backend and junior and pizza 100",
                    "python and frontend and senior and chicken 200",
                    "cpp and - and senior and pizza 250",
                    "- and backend and senior and - 150",
                    "- and - and - and chicken 100",
                    "- and - and - and - 150"]))
