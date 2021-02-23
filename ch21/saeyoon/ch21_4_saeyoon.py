"""
## 21-4. 주유소

원형으로 경로가 연결된 주유소 목록이 있다.
각 주유소는 gas[i] 만큼의 기름을 갖고 있으며， 다음 주유소로 이동하는데 cost[i]가 필요하다.
기름이 부족하면 이동할 수 없다고 할 때 모든 주유소를 방문할 수 있는 출발점의 인멕스를 출력하라.

출발점이 존재하지 않을경우 -1을 리턴하며，출발점은 유일하다.
"""
from typing import *


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 44ms

        # 출발점이 무조건 존재하지 않는 경우
        if sum(gas) < sum(cost):
            return -1

        start, fuel = 0, 0
        for i in range(len(gas)):
            fuel += gas[i] - cost[i]
            if fuel < 0:
                start = i + 1
                fuel = 0

        return start


if __name__ == '__main__':
    sol = Solution()
    print(sol.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))