"""
## 추석 트래픽
"""
from typing import *
from datetime import datetime


def solution(lines: List[str]) -> int:
    def count_log(t):
        cnt = 0
        for time in times:
            if time[0] < t + 1 and time[1] >= t:
                cnt += 1
        return cnt

    # 로그 시각 저장
    times = []
    for line in lines:
        *S, T = line.split()
        timestamp = datetime.strptime(S[0] + ' ' + S[1], "%Y-%m-%d %H:%M:%S.%f").timestamp()
        times.append((timestamp - float(T[:-1]) + 0.001, timestamp))

    max_cnt = 0
    for time in times:
        max_cnt = max(max_cnt, count_log(time[0]), count_log(time[1]))

    return max_cnt


if __name__ == '__main__':
    print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
    print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
    print(solution(["2016-09-15 20:59:57.421 0.351s",
                     "2016-09-15 20:59:58.233 1.181s",
                     "2016-09-15 20:59:58.299 0.8s",
                     "2016-09-15 20:59:58.688 1.041s",
                     "2016-09-15 20:59:59.591 1.412s",
                     "2016-09-15 21:00:00.464 1.466s",
                     "2016-09-15 21:00:00.741 1.581s",
                     "2016-09-15 21:00:00.748 2.31s",
                     "2016-09-15 21:00:00.966 0.381s",
                     "2016-09-15 21:00:02.066 2.62s"]))