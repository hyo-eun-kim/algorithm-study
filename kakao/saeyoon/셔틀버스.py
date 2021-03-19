"""
## 셔틀버스
"""
from typing import *


def solution(n: int, t: int, m: int, timetable: List[str]) -> str:
    timetable = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]
    timetable.sort()

    current = 540
    for i in range(n):
        for j in range(m):
            if timetable and timetable[0] <= current:
                end = timetable.pop(0) - 1 # 콘은 무조건 타야하므로 1분 빠른 시각으로 설정
            else:
                end = current
        current += t

    h, m = divmod(end, 60)
    return str(h).zfill(2) + ':' + str(m).zfill(2)


if __name__ == '__main__':
    print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
    print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
    print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))