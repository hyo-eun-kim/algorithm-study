"""
## 21-3. 태스크 스케줄러
A에서 Z로 표현된 태스크가 있다.
각 간격마다 CPU는 한 번의 태스크만 실행할 수 있고，
n번의 간격 내에는 동일한 태스크를 실행할 수 없다.
더 이상 태스크를 실행할 수 없는 경우 아이들 idle 상태가 된다.
모든 태스크를 실행하기 위한 최소 간격을 출력하라.
https://leetcode.com/problems/task-scheduler/
"""
from typing import *
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        counter = Counter(tasks)
        task_sorted = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        for i, (task, freq) in enumerate(task_sorted):
            if i == 0:
                max_freq = freq
                idle_time = n * (freq - 1)
            else:
                idle_time -= min(max_freq - 1, freq)
            if idle_time <= 0:
                break
        return max(len(tasks) + idle_time, len(tasks))


if __name__ == '__main__':
    sol = Solution()
    print(sol.leastInterval(["A", "A", "A", "B", "B", "B"], 2))
    print(sol.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2))